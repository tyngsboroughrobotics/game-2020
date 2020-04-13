import time
from .configuration import MotorConfiguration, WheelsConfiguration
from .helpers import run_in_background, forward, reverse, left, right
from .libwallaby import libwallaby
from .motor import Motor


class Wheels(object):
    '''
    A controller for managing two motors acting as wheels, to allow for easily
    moving them in unison.

    Usually, the left and right motors won't be perfectly in alignment; you can
    multiply their speeds individually with the `left_offset` and `right_offset`
    properties. Note that these properties are very sensitive; you probably only
    need to adjust them by a small amount to get your wheels going straight!
    '''

    def __init__(self, left_motor, right_motor, left_offset=1, right_offset=1):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_offset = left_offset
        self.right_offset = right_offset

    def drive(self, direction, cm):
        '''
        Move both wheels the specified distance (in cm) in the specified
        direction (`forward` or `reverse`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        # Calculate the velocities for each motor separately, incorporating
        # the offset
        left_velocity = self._velocity(self.left_motor.speed, direction, self.left_offset)
        right_velocity = self._velocity(self.right_motor.speed, direction, self.right_offset)

        # Whichever motor travels slower, sleep for that amount of time
        if left_velocity < right_velocity:
            sleep_time = Motor._block_duration(cm, left_velocity)
        else:
            sleep_time = Motor._block_duration(cm, right_velocity)

        # Drive the motors in unison and sleep
        self._drive(left_velocity, right_velocity, sleep_time)

    def turn(self, direction, degrees):
        '''
        Turn both wheels the specified amount (in degrees) in the specified
        direction (`left` or `right`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        # Determine which direction each wheel should move depending on the
        # direction of the turn
        if direction == left:
            left_direction = reverse
            right_direction = forward
        else:
            left_direction = forward
            right_direction = reverse

        # Calculate the velocities for each motor separately, ignoring the
        # offset because it is not applicable while turning
        left_velocity = self._velocity(self.left_motor.speed, left_direction, 1)
        right_velocity = self._velocity(self.right_motor.speed, right_direction, 1)

        # Determine how long to sleep while the turn occurs
        cm = WheelsConfiguration.turn_amount(degrees)
        sleep_time = Motor._block_duration(cm, left_velocity)

        # Drive the motors in unison and sleep
        self._drive(left_velocity, right_velocity, sleep_time)

    def _drive(self, left_velocity, right_velocity, sleep_time):
        '''
        Drive both motors in unison at the specified velocities and sleep.
        '''

        libwallaby.move_at_velocity(self.left_motor.port, left_velocity)
        libwallaby.move_at_velocity(self.right_motor.port, right_velocity)

        time.sleep(sleep_time)

        libwallaby.off(self.left_motor.port)
        libwallaby.off(self.right_motor.port)

    def _velocity(self, speed, direction, offset):
        '''
        Replacement for `Motor`'s velocity calculation incorporating the wheel
        offset.
        '''

        velocity = int(speed * MotorConfiguration.pwm_ticks * offset)

        if direction == reverse:
            velocity *= -1

        return velocity

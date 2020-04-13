import time
from .configuration import MotorConfiguration
from .helpers import reverse
from .libwallaby import libwallaby

class Motor(object):
    '''
    Represents a motor connected to the robot. You can control it with the
    `drive` method. The default speed for the motor is 1.0 and must be between 0
    and 1 (1 being the fastest).
    '''

    def __init__(self, port, speed = 1.0):
        self.port = port
        self.speed = speed

    def drive(self, direction, cm):
        '''
        Move the motor the specified distance (in cm) in the specified direction
        (`forward` or `reverse`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        # Calculate the raw velocity the motor should travel from the current
        # speed
        velocity = int(self.speed * MotorConfiguration.pwm_ticks)

        if direction == reverse:
            velocity *= -1

        # Move the motor at the calculated velocity
        libwallaby.move_at_velocity(self.port, velocity)

        # Calculate how long it will take the motor to travel
        block_duration = Motor._block_duration(cm, velocity)

        # Block until the motor has finished traveling the specified distance
        time.sleep(block_duration)

        # Turn off the motor
        libwallaby.off(self.port)

    @staticmethod
    def _block_duration(cm, velocity):
        return abs(MotorConfiguration.pwm_ticks * MotorConfiguration.travel_time_1_cm * cm / velocity)

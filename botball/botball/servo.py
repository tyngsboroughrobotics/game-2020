import time
from .libwallaby import libwallaby
from .helpers import scale
from .configuration import ServoConfiguration


class Servo(object):
    '''
    Represents a servo motor connected to the robot. You can control it by
    setting the `position` property to a value between 0 and 1.
    '''

    def __init__(self, port):
        self.port = port

    @property
    def position(self):
        '''
        The current position of the servo, between 0 and 1. The meaning of this
        position depends on how your servo is oriented.
        '''

        raw_position = libwallaby.get_servo_position(self.port)
        return scale(raw_position, ServoConfiguration.raw_position_range(), range(0, 1))

    def set_position(self, position):
        '''
        Set the position of this servo to a value between 0 and 1. The meaning
        of this position depends on how your servo is oriented.

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple servos at once),
        change this value on a background thread. This class is not necessarily
        thread-safe.
        '''

        # Enable this servo
        libwallaby.enable_servo(self.port)

        # Move the servo to the specified position
        raw_position = scale(position, range(0, 1), ServoConfiguration.raw_position_range())
        libwallaby.set_servo_position(int(raw_position))

        # Wait until the servo finishes moving
        time.sleep(ServoConfiguration.sleep_amount)

        # Disable this servo while we're not using it to save battery life
        libwallaby.disable_servo(self.port)

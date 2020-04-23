import time
from .libwallaby import *
from .configuration import CreateConfiguration
from .helpers import reverse


class Create(object):
    '''
    Allows you to control an iRobot Create connected to the robot. The default
    speed for the Create is 1.0 and must be between 0 and 1 (1 being the
    fastest.)
    '''

    def __init__(self, speed=1.0):
        self.speed = speed

        libwallaby.create_connect()

    def drive(self, direction, cm):
        '''
        Move the Create the specified distance (in cm) in the specified
        direction (`forward` or `reverse`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        velocity = int(self.speed * CreateConfiguration.max_velocity)

        if direction == reverse:
            velocity *= -1

        # Start driving the Create
        libwallaby.create_drive_straight(velocity)

        # Figure out how long to sleep as the Create travels
        block_duration = Create._block_duration(cm, velocity)

        # Block until the Create has finished traveling the specified distance
        time.sleep(block_duration)

        # Turn off the Create
        libwallaby.create_stop()


    def turn(self, direction, degrees):
        '''
        Turn the Create the specified amount (in degrees) in the specified
        direction (`left` or `right`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        pass  # TODO

    @staticmethod
    def _block_duration(cm, velocity):
        return abs(CreateConfiguration.max_velocity * CreateConfiguration.travel_time_1_cm * cm / velocity)

from .libwallaby import *
from .configuration import CreateConfiguration


class Create(object):
    '''
    Allows you to control an iRobot Create connected to the robot.
    '''

    def __init__(self):
        libwallaby.create_connect()

    def drive(self, direction, cm):
        '''
        Move the Create the specified distance (in cm) in the specified
        direction (`forward` or `reverse`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        # TODO: In the future we might want to support custom speeds like Motor
        velocity = CreateConfiguration.max_velocity

        if direction == reverse:
            velocity *= -1

        # Start driving the Create
        libwallaby.create_drive_straight(velocity)

        # Figure out how long to sleep as the Create travels
        block_duration = cm * CreateConfiguration.travel_time_1_cm

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

from .libwallaby import *


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

        pass  # TODO

    def turn(self, direction, degrees):
        '''
        Turn the Create the specified amount (in degrees) in the specified
        direction (`left` or `right`).

        Note that this function blocks until finished; if you don't want to
        block the current thread (eg. to control multiple motors at once), call
        it on a background thread. This class is not necessarily thread-safe.
        '''

        pass  # TODO

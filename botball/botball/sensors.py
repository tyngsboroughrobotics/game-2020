from .libwallaby import libwallaby
from .helpers import scale


class DigitalSensor(object):
    '''
    Represents a digital sensor connected to the robot.
    '''

    def __init__(self, port):
        self.port = port

    @property
    def value(self):
        '''
        Returns a boolean value representing whether the sensor is activated or
        not.
        '''

        return bool(libwallaby.digital(self.port))


class AnalogSensor(object):
    '''
    Represents an analog sensor connected to the robot.
    '''

    def __init__(self, port):
        self.port = port

    @property
    def value(self):
        '''
        Returns a value between 0 and 1 representing the state of the sensor.
        '''

        return scale(self.raw_value, range(0, 4095), range(0, 1))

    @property
    def raw_value(self):
        '''
        Returns an integer value between 0 and 4095 representing the raw state
        of the sensor.
        '''

        return libwallaby.analog(self.port)

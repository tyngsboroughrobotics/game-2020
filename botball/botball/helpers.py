from datetime import datetime, timedelta


forward = '__forward__'
'''
Used to represent the forward direction on wheels and motors.
'''

reverse = '__reverse__'
'''
Used to represent the reverse direction on wheels and motors.
'''

left = '__left__'
'''
Used to represent the left/counterclockwise direction on wheels and motors.
'''

right = '__right__'
'''
Used to represent the right/clockwise direction on wheels and motors.
'''


def scale(number, start_range, end_range):
    '''
    Scales a number from one range to another.
    '''

    (in_min, in_max) = (start_range.start, start_range.stop)
    (out_min, out_max) = (end_range.start, end_range.stop)

    return (number - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def run_in_background(block):
    '''
    Run `block` on a background thread.
    '''

    from threading import Thread

    thread = Thread(target=block)
    thread.daemon = True
    thread.start()


class Timer:
    '''
    Helper to track the duration between the time the `Timer` object was created
    and the time `time_elapsed` is accessed.
    '''

    def __init__(self):
        self.start_date = datetime.now()

    @property
    def time_elapsed(self):
        '''
        The amount of time elapsed since this `Timer` object was created, in
        seconds.
        '''

        end_date = datetime.now()
        difference = end_date - self.start_date
        return difference.total_seconds()

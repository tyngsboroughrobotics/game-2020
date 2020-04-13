from botball import *

class Arm(Servo):
    def raise_up(self):
        self.set_position(0.25)

    def lower_down(self):
        self.set_position(0.6)

    def reset(self):
        self.set_position(0.9)

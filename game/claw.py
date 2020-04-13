from botball import *

class Claw(Servo):
    def open(self):
        self.set_position(0.7)

    def close(self):
        self.set_position(0.15)

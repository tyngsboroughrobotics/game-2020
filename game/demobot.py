from botball import *
from .claw import Claw

left_wheel = Motor(port=0)
right_wheel = Motor(port=1)
wheels = Wheels(left_wheel, right_wheel, right_offset=1.05)

claw = Claw(port=0)

# Move forward
def step_move_forward():
    wheels.drive(forward, cm=10)

# Pick up the block
def step_pick_up_block():
    claw.open()
    wheels.drive(forward, cm=1)
    claw.close()
    wheels.drive(reverse, cm=1)

# Turn around and go back to the start
def step_back_to_start():
    wheels.turn(left, 180)
    wheels.drive(forward, cm=10)

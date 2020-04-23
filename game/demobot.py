from botball import *
from .claw import *
from .arm import *

left_wheel = Motor(port=0)
right_wheel = Motor(port=1)
wheels = Wheels(left_wheel, right_wheel, left_offset=1.05)

claw = Claw(port=0)
arm = Arm(port=1)


# Test run
def step_test_run():
    arm.lower_down()
    wheels.drive(forward, cm=16)


# Move up to and grab material transport
def step_grab_material_transport():
    arm.lower_down()
    claw.open()
    wheels.drive(forward, cm=18)
    claw.close()
    wheels.drive(reverse, cm=33.5)


# Move material transport to mine
def step_move_near_the_mine():
    wheels.turn(right, 140)
    wheels.drive(forward, cm=30)
    claw.open()


# Move to the bottom of the ramp
def step_move_to_bottom_ramp():
    # Drive toward the edge of the table
    wheels.drive(reverse, cm=29)

    # Turn to face toward the ramp
    wheels.turn(right, 95)

    # Drive toward the ramp
    wheels.drive(reverse, cm=27)

    # Raise the arm to it doesn't hit the ramp
    arm.raise_up()

    # The space between the ramp and the edge of the board isn't wide enough for
    # us to make a straight 90-degree turn, so we have to inch forward and keep
    # turning
    right_wheel.drive(reverse, cm=8)
    wheels.drive(reverse, cm=15)

    # At this point the left wheel is aligned with the bottom of the ramp, so
    # we just need the right wheel to move so the robot is perfectly aligned
    # with the ramp
    right_wheel.drive(reverse, cm=35)


# Drive up the ramp
# The sliding arm should be facing toward the ramp and the front of the wheels
# should be touching the bottom of the ramp. The robot should be centered as it
# goes up the ramp.
def step_drive_up_ramp():
    wheels.drive(reverse, cm=94)

from botball.core import step, Direction
from botball.core.procedure import Procedure
from botball.core.components import Motor, WheelGroup, Servo

# - Components

left_wheel = Motor(port=1, speed=1)
right_wheel = Motor(port=0, speed=1)
wheels = WheelGroup(left_wheel, right_wheel)
arm = Servo(port=1, speed=1)
claw = Servo(port=2, speed=1)

def raise_arm():
    arm.set_position_to(0.3)

def lower_arm():
    arm.set_position_to(0.0)

def open_claw():
    claw.set_position_to(0.0)

def close_claw():
    claw.set_position_to(0.5)

# - Steps

@step(name="Test")
def test():
    open_claw()
    raise_arm()

    # Move to the block
    wheels.drive(mm=120)

    # Pick up the block
    lower_arm()
    close_claw()
    raise_arm()

    # Move back to the start
    wheels.drive(Direction.Backward, mm=120)

    # Drop the block
    open_claw()

# - Procedure

procedure = Procedure(name="demobot", steps=[
    test,
])

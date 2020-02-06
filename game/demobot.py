from botball import *

# - Components

left_wheel = Motor(port=1, speed=1.0)
right_wheel = Motor(port=0, speed=1.0)
wheels = WheelGroup(left_wheel, right_wheel, right_offset=1.6)

arm = Servo(port=0)
claw = Servo(port=1)

left_rear_button = DigitalSensor(port=1)
right_rear_button = DigitalSensor(port=0)

# - Steps

@step(name="Move up to block")
def move_up_to_block():
    wheels.drive(mm=100)

@step(name="Grab block")
def grab_block():
    lower_arm()
    open_claw()
    wheels.drive(mm=50)
    close_claw()
    raise_arm()
    wheels.drive(Direction.Backward, mm=50)

@step(name="Go back")
def go_back():
    wheels.drive(Direction.Backward, mm=100)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move_up_to_block,
    grab_block,
    go_back,
])

# - Helpers

def raise_arm():
    arm.set_position_to(0.5)

def lower_arm():
    arm.set_position_to(0.8)

def close_claw():
    claw.set_position_to(0.45)

def open_claw():
    claw.set_position_to(0.1)

from botball.core.procedure import step, Procedure

# - Components

# Initialize your motors, servos, and sensors here, eg:
#
# from botball.core.components import Motor, WheelGroup
# left_motor = Motor(port=0, speed=1.0)
# right_motor = Motor(port=1, speed=1.0)
# wheels = WheelGroup(left_motor, right_motor)

# - Steps

# Define your steps here, eg:
#
# @step(name=..., description=...)
# def ...():
#     wheels.drive(Direction.Forward, mm=100)

# - Procedure

# Build your procedure here, eg:
#
procedure = Procedure(name=..., steps=[
    ...
])

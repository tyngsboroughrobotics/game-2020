from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction

# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

# - Steps

@step(name="test")
def test():
    wheels.drive(Direction.Forward, mm=100)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    test,
])

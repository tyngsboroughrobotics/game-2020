from botball.core import step
from botball.core.procedure import Procedure
from botball.core.components import Motor, WheelGroup, Servo

# - Components

left_wheel = Motor(port=3, speed=1)
right_wheel = Motor(port=0, speed=1)
wheels = WheelGroup(left_wheel, right_wheel)
arm = Servo(port=0, speed=1)
# - Steps

@step(name="Move")
def move():
    arm.set_position_to(0.4)
    wheels.drive(mm=180)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move,
])

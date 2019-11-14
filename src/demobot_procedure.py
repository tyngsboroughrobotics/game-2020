from time import sleep

from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction, Servo

print("Hello from Wilson!")
print("Hello from Aman")
print("Hello from Tirth")
# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

arm_servo = Servo(port=5, speed=1.0)

# - Steps

@step(name="Move", description="Moves across the table")
def move():
    wheels.turn_right(45)
    wheels.turn_left(45)

    sleep(1)

    wheels.turn_right(90)
    wheels.turn_left(90)

    sleep(1)

    wheels.turn_right(180)
    wheels.turn_left(180)

    sleep(1)

    wheels.turn_right(360)
    wheels.turn_left(360)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move,
])

from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction, Servo

# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

arm_servo = Servo(port=5, speed=1.0)

# - Steps

@step(name="Move", description="Moves across the table")
def move():
    wheels.drive(mm=300)
    wheels.turn_left(70)

    arm_servo.set_position_to(0.5)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move.repeat(2),
])

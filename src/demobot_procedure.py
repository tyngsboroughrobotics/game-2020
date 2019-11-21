from botball.core.helpers import scale
from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction, Servo
from botball.core.components.devices.camera import Camera

# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

arm_servo = Servo(port=5, speed=1.0)

# - Steps

@step(name="Move", description="Moves across the table")
def move():
    with Camera(tracking_color="red") as camera:
        while True:
            if camera.object_is_present():
                bbox = camera.object_bbox()

                # Map the position of the object in the camera frame to a servo
                # position between 0 and 1
                servo_position = scale(bbox.y, 0, camera.height, 0, 1)

                # TODO: Finish

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move,
])

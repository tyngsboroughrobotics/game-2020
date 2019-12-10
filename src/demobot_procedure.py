from botball.core.helpers import scale
from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction, Servo
from botball.core.components.devices.camera import Camera

import os

# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

arm_servo = Servo(port=2, speed=1.0)

# - Steps

@step(name="Move", description="Moves across the table")
def move():
    print("Connecting...")

    with Camera(tracking_color="red") as camera:
        print("camera is connected")
        while True:
            if camera.object_is_present() and camera.object_is_trackable():
                bbox = camera.object_bbox()
                print(f"bbox: x={bbox.ulx} y={bbox.uly} w={bbox.width} h={bbox.height}")

                # Map the position of the object in the camera frame to a servo
                # position between 0 and 1
                servo_position = scale(bbox.uly, 0, camera.height, 0, 1)
                print(f"servo_position: {servo_position}")

                arm_servo.set_position_to(servo_position)
            else:
                print("Object NOT present")

            camera.refresh(1)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move,
])

from botball.core.helpers import scale
from botball.core.procedure import step, Procedure
from botball.core.components import Motor, WheelGroup, Direction, Servo
from botball.core.components.devices.camera import Camera

# - Components

print(11111)

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor)

arm_servo = Servo(port=2, speed=1.0)

print(22222)

#####################################################
#####################################################
## TODO: STOP PYTHON FROM GENERATING PYC FILES!!!! ##
#####################################################
#####################################################

# - Steps

@step(name="Move", description="Moves across the table")
def move():
    print("Connecting...")

    with Camera(tracking_color="red") as camera:
        print("camera is connected")
        while True:
            print("foo")
            # if camera.object_is_present():
            #     bbox = camera.object_bbox()
            #
            #     # Map the position of the object in the camera frame to a servo
            #     # position between 0 and 1
            #     servo_position = scale(bbox.uly, 0, camera.height, 0, 1)
            #     print(servo_position)
            #
            #     arm_servo.set_position_to(servo_position)

# - Procedure

procedure = Procedure(name="demobot", steps=[
    move,
])

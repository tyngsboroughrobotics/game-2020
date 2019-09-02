from botball.core.components import Motor, WheelGroup, Servo, Direction
from botball.core.components.devices import Camera
from botball.core.procedure import step, Procedure

# The right motor veers off a bit, so we make the left wheel a bit slower to
# have the robot move in a straight line
left_motor_offset = 0.98
right_motor_offset = 1.0

# - Initialize components

left_motor = Motor(port=1, speed=1.0)
right_motor = Motor(port=3, speed=1.0)

wheels = WheelGroup(
    left_motor,
    right_motor,
    left_motor_offset,
    right_motor_offset
)

arm_servo = Servo(port=3, speed=0.7)

# - Game procedure methods

@step(name="Reset servos")
def reset_servos():
    arm_servo.set_position_to(0.2)

@step(
    name="Get the ambulance",
    description="Grab the ambulance on the right edge of the starting block"
)
def get_ambulance():
    # From the starting block, turn and face the ambulance. Put the plow down
    # and drive it over to the ambulance so it's in the plow.

    arm_servo.set_position_to(0)
    wheels.turn_right(degrees=7.5)
    arm_servo.set_position_to(0.32)  # touch the table

    wheels.drive(mm=280)
    wheels.turn_left(degrees=140)

@step(
    name="Drive over to buildings",
    description="Drive over with the ambulance to the burning buildings"
)
def drive_to_buildings():
    wheels.drive(mm=1350)

# Store which building is burning so we know which building is safe later on.
burning_building = None

@step(
    name="Put ambulance in safe building",
    description="Check which building is the safe one, and dispense the ambulance in front of it."
)
def put_ambulance_in_safe_building():
    # Determine which building is burning and which is safe

    with Camera(tracking_color="yellow") as camera:
        # Make sure that both a yellow AND red object is present (the marker is
        # yellow with a red circle in the middle)

        yellow_present = camera.object_is_trackable()

        camera.tracking_color = "red"
        red_present = camera.object_is_trackable()

        global burning_building
        burning_building = "first" if yellow_present and red_present else "second"

    # Place the ambulance in the safe building

    if burning_building == "first":
        # The second building is the safe one; drive up to it so we can dispense
        # The ambulance there instead

        wheels.turn_right(degrees=45)
        wheels.drive(mm=250)

    # Drive right up to the building and dispense the ambulance

    wheels.drive(mm=50)
    wheels.drive(Direction.Backward, mm=100)

@step(
    name="Pick up firetruck",
    description="Drive back to the start and obtain the firetruck"
)
def pick_up_firetruck():
    if burning_building == "first":
        # Turn around and grab the firetruck cube
        wheels.drive(Direction.Backward, mm=530)
        wheels.turn_right(degrees=135)
        wheels.drive(mm=240)

        # Drive up to the building
        wheels.turn_left(degrees=245)
        wheels.drive(380)
    else:
        # Turn around and grab the firetruck cube
        wheels.turn_left(degrees=245)
        wheels.drive(mm=380)

        # Drive up to the building
        wheels.turn_left(degrees=242)
        wheels.drive(mm=700)
        wheels.drive(Direction.Backward, mm=350)

        # Turn around to the black line
        wheels.turn_right(degrees=180)

# - Game procedure

procedure = Procedure(name="Demobot Temp", steps=[
    reset_servos, # reset everything at the start of the game

    get_ambulance,
    drive_to_buildings,
    put_ambulance_in_safe_building,
    pick_up_firetruck,

    reset_servos, # reset everything at the end of the game, too
])

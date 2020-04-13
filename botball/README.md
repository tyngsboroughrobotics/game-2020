# Botball for Python

<p align="center">
  <img src="https://i.postimg.cc/3NZfHT1n/THS-Robotics-Logo-Dual.png" height=240>
</p>

Botball for Python provides Python wrappers for several Botball components (including motors, servos, sensors and wheels), an interface for organizing your robot's code through games and steps, and access to the entire `libwallaby` C library so it can interoperate with existing projects. Botball for Python is designed for Python 3 and is fully documented.

### [Documentation](https://tyngsboroughrobotics.github.io/game/botball/docs/)

## Example

```python
from botball import *

# Inherit from builtin components to provide additional functionality
class Claw(Servo):
    def open(self):
        self.set_position(0.7)

    def close(self):
        self.set_position(0.15)

# Declare your motors and sensors with plain variables
claw = Claw(port=0)
left_wheel = Motor(port=0)
right_wheel = Motor(port=1)

# A builtin controller for managing wheels, with offsets to keep them straight
wheels = Wheels(left_wheel, right_wheel, right_offset=1.05)

# Organize your code with "steps" -- just prefix the function with "step_"
def step_move_forward():
    # Calls to motors and wheels wait until they are finished before returning,
    # so you don't need to manually delay -- use actual distance units instead!
    wheels.drive(forward, cm=10)

def step_pick_up_block():
    claw.open()
    wheels.drive(forward, cm=1)
    claw.close()
    wheels.drive(reverse, cm=1)

def step_turn_back_to_start():
    # Turning is as simple as passing in the amount in degrees
    wheels.turn(left, 180)
    wheels.drive(forward, cm=10)
```

Botball for Python automatically detects the functions in your code labeled `step_` and organizes them into a `Game` object, which you can then run. It also times how long each step takes to run, so you can ensure your robot finishes within the time limit.

## Generating documentation

Run `python make_docs.py`. The documentation will be available in the `docs/` folder.

## Contributing

We welcome all contributions to Botball for Python — feel free to submit an issue or pull request!

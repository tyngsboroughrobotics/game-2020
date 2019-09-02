import subprocess as sp

from botball.core import step, Procedure
from botball.core.components.devices import Motor, WheelGroup
from botball.core.components.sensors import AnalogSensor, LightSensor, DigitalSensor

# - Components

left_motor = Motor(port=0, speed=1.0)
right_motor = Motor(port=1, speed=1.0)
wheels = WheelGroup(left_motor, right_motor, right_offset=0.98)

light_sensor = LightSensor(port=0)
slider = AnalogSensor(port=1)
proximity_sensor = AnalogSensor(port=2)

long_button = DigitalSensor(port=0)
top_hat = DigitalSensor(port=1)

# - Steps

@step(name="Demo")
def demo():
    while True:
        sp.call('clear', shell=True)

        print(f"Light sensor: {light_sensor.percent_value()}")
        print(f"Slider: {slider.percent_value()}")
        print(f"Proximity sensor: {proximity_sensor.percent_value()}")
        print()
        print(f"Long button: {'Pressed' if long_button.value() else 'Not pressed'}")
        print(f"Top hat: {'Black' if top_hat.value() else 'White'} surface")

# - Procedure

procedure = Procedure(name="Demobot", steps=[
    demo,
])

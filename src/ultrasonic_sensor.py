import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
import RPi.GPIO as GPIO
import time
import json

# Class for MySensor
class MySensor(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("nyu", "hc-sr04-sensor"), "linux")

    def __init__(self, name: str, trig_pin: int, echo_pin: int):
        super().__init__(name)
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

        # Initialize GPIO for the sensor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> "MySensor":
        # Read configuration from config.json
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            sensor_config = next(item for item in config_data["components"] if item["name"] == config.name)
            trig_pin = sensor_config["attributes"]["trigger_pin"]
            echo_pin = sensor_config["attributes"]["echo_pin"]
            sensor = cls(config.name, trig_pin, echo_pin)
            return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        # Trigger the sensor and read the distance
        GPIO.output(self.trig_pin, False)
        time.sleep(2E-6)
        GPIO.output(self.trig_pin, True)
        time.sleep(10E-6)
        GPIO.output(self.trig_pin, False)

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        ping_travel_time = stop_time - start_time

        # Distance calculation in inches
        distance = 767 * ping_travel_time * 5280 * 12 / 3600
        distance = distance / 2
        return {"distance_in_inches": round(distance, 1)}

async def main():
    sensor = await MySensor.new(ComponentConfig(name="hc-sr04"), {})
    reading = await sensor.get_readings()
    print(reading)

# Run the main function when the script is executed
if __name__ == '__main__':
    asyncio.run(main())

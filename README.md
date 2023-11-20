# HC-SR04 Ultrasonic Sensor Module for Raspberry Pi
This repository contains a Viam-compatible module that enables a Raspberry Pi to measure distances using the HC-SR04 ultrasonic sensor. This module integrates with Viam's robotics platform, allowing for precise distance measurements in your robotics projects.
## Getting Started

### Prerequisites

- Raspberry Pi (with GPIO pins)
- HC-SR04 Ultrasonic Distance Sensor
- Viam account and CLI tool installed

Viam account and CLI tool installed

### Installation

1. Clone the repository to your Raspberry Pi:
   ```shell
   git clone https://github.com/Gaurang-1402/viam_hc-sr04_sensor.git
   cd viam_hc-sr04_sensor

   ```
## Contents

- src: folder with python code
- exec.sh, setup.sh: entrypoint and dependencies setup for when this runs as a module on a robot
- Makefile: bundles your module into a tarball for distribution
- .github/workflows: uploads the module when you do a github release
- meta.json: Viam module configuration file
- requirements.txt: dependencies. When run as a module, setup.sh installs these in the virtualenv

## Install the Python dependencies:
```shell
pip install -r requirements.txt
```
## Configuration

Configuration
The config.json file is crucial for setting the correct GPIO pin numbers for the HC-SR04 sensor. Modify this file to match your sensor's wiring:

```json
   {
       "components": [
           {
               "name": "ultrasonic_sensor",
               "type": "sensor",
               "model": "nyu:hcsr04:linux",
               "attributes": {
                   "trigger_pin": 23,
                   "echo_pin": 24
               },
               "depends_on": []
           }
       ]
   }

```
Ensure the trigger_pin and echo_pin values match the GPIO pins you've connected the HC-SR04 sensor to on your Raspberry Pi.

Update meta.json with your module information and Viam account details.
Modify config.json to set the correct GPIO pin number and any other configurations for the DHT11 sensor.

Update meta.json with your module information and Viam account details.

## Usage
After uploading, the module can be added to your Viam robot configuration. It will periodically read distance readings from the HC-SR04 sensor and update the readings on the Viam platform.

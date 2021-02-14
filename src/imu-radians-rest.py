import json
import requests
from sense_hat import SenseHat
import time

class SenseHatCSV:

    ETX = [255, 0, 0]
    OFF = [0, 0, 0]  # off
    BTX = [0, 255, 0]  # on

    led_tx_on = [
        BTX, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF
    ]

    led_tx_off = [
        ETX, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF,
        OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF
    ]

    RADIANS = "RADIANS"
    ACCEL = "ACCEL"
    GYRO = "GYRO"

    def __init__(self, config):
        self.sense = SenseHat()
        self.config = config


    def make_post_call(self):
        imu_data = self.sense.get_orientation_radians()
        data = {
            'xRoll': self.imu_input['pitch'],
            'yPitch': self.imu_input['roll'],
            'zYaw': self.imu_input['yaw'],
            'experimentId': self.experiment_id,
            'type': self.sensor_type,
            'sensorLocation': sensor_location,
            'subject': subject,
            'isRaw': False,
            'timestamp': round(time.time() * 1000),
            'deviceId': inputDeviceId
        }
        sense.set_pixels(led_tx_on)
        requests.post(rest_endpoint, json=data)
        sense.set_pixels(led_tx_off)

while (True):
    imu_data = sense.get_orientation_radians()
    make_post_call(imu_data)

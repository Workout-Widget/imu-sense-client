import json
import requests
from sense_hat import SenseHat
import time

class SenseHatREST:

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

    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_imu_config(True, True, True)


    def get_record_from_radians(self):
        imu_input = self.sense.get_orientation_radians()
        data = {
            'xRoll': imu_input['pitch'],
            'yPitch': imu_input['roll'],
            'zYaw': imu_input['yaw'],
            'timestamp': round(time.time() * 1000),
        }
        return data

    def make_post_call(self, data, config):
        
        data['experimentId'] = config.get('experiment_id'),
        data['type'] = config.get('sensor_type'),
        data['sensorLocation'] = config.get('sensor_location'),
        data['subject'] = config.get('subject'),
        data['exercise'] = config.get('exercise'),
        data['isRaw'] = config.get('False'),
        data['timestamp'] = round(time.time() * 1000),
        data['deviceId'] = config.get('inputDeviceId')

        sense.set_pixels(led_tx_on)
        requests.post(config.get('restEndpoint'), json=data)
        sense.set_pixels(led_tx_off)


if __name__ == "__main__":

    sense_hat_rest = SenseHatREST()

    print("Welcome to the Workout Widget REST SenseHAT Client!")
    print("Please configure your test by answering the following questions...")

    rest_endpoint = input("REST API endpoint: (ex: http://127.0.0.1:8080/motion/): ")
    experiment_id = input("String-based experiment ID: ")

    sensor_type = ""
    usr_choice = ""

    while True:
        usr_choice = input("What sensor type are you using?\n\t1) RADIANS\n\t2) ACCEL\n\t3) GYRO\n")
        if usr_choice == "1":
            sensor_type = sense_hat_rest.RADIANS
            break
        elif usr_choice == "2":
            sensor_type = sense_hat_rest.ACCEL
            break
        elif usr_choice == "3":
            sensor_type = sense_hat_rest.GYRO
            break
        else:
            print("Invalid choice, please try again...")

    inputDeviceId = input("Please enter a device ID: ")
    sensor_location = input("Where is the IMU located? ")
    exercise = input("Please enter the exercise being recorded: ")
    subject = input("Who is wearing the IMU? ")

    config = {
        'restEndpoint': rest_endpoint,
        'experimentId': experiment_id,
        'type': sensor_type,
        'sensorLocation': sensor_location,
        'subject': subject,
        'exercise': exercise,
        'isRaw': False,
        'timestamp': round(time.time() * 1000),
        'deviceId': inputDeviceId
    }

    while True:
        data = sense_hat_rest.get_record_from_radians()
        sense_hat_rest.make_post_call(data, config)

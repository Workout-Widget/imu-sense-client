import json
import requests
from sense_hat import SenseHat

sense = SenseHat()

ETX = [255, 0, 0]
OFF = [0, 0, 0]  # off
BTX = [0, 255, 0]  # on

rest_endpoint = "http://178.168.1.184:8080/motion/"
experiment_id = "dummy experiment"
sensorType = "ORIENTATION RADIANS"
inputDeviceId = "LEE"
sensor_location = "LEFT WRIST"
exercise = "STANDING DUMBELL BICEP CURL"
subject = "dummy subject"

led_tx_on = [
    BTX,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF
]

led_tx_off = [
    ETX,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
    OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF
]

def make_post_call(imu_input):
    data = {
        'xRoll': imu_input['pitch'],
        'yPitch': imu_input['roll'],
        'zYaw': imu_input['yaw'],
        'experimentId': experiment_id,
        'type': sensorType,
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

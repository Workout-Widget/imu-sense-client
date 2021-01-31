import requests
import json
import time

rest_endpoint = "http://127.0.0.1:8080/motion/"
experiment_id = "NA"
sensorType = "NA"
inputDeviceId = "NA"
sensor_location = "NA"
exercise = "NA"
subject = "NA"

def make_post_call():
    data = {
        'xRoll': 0.1,
        'yPitch': 0.2,
        'zYaw': 0.3,
        'experimentId': experiment_id,
        'type': sensorType,
        'sensorLocation': sensor_location,
        'subject': subject,
        'isRaw': False,
        'timestamp': round(time.time() * 1000),
        'deviceId': inputDeviceId
    }
    requests.post(rest_endpoint, json=data)

while (True):
    make_post_call()
    time.sleep(.3)

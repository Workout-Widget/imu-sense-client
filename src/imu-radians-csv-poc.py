from sense_hat import SenseHat
import time
import json


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

    def __init__(self):
        self.sense = SenseHat()


    def get_record_from_radians(self):
        imu_input = self.sense.get_orientation_radians()
        data = {
            'xRoll': imu_input['pitch'],
            'yPitch': imu_input['roll'],
            'zYaw': imu_input['yaw'],
            'timestamp': round(time.time() * 1000),
        }
        return data


if __name__ == "__main__":

    sense_hat_csv = SenseHatCSV()

    print("Welcome to the Workout Widget CSV SenseHAT Client!")
    print("Please configure your test by answering the following questions...")

    experiment_id = input("String-based experiment ID: ")


    sensor_type = ""
    usr_choice = ""

    while True:
        usr_choice = input("What sensor type are you using?\n\t\t1) RADIANS\n\t\t2) ACCEL\n\t\t3) GYRO\n")
        if usr_choice == "1":
            sensor_type = sense_hat_csv.RADIANS
            break
        elif usr_choice == "2":
            sensor_type = sense_hat_csv.ACCEL
            break
        elif usr_choice == "3":
            sensor_type = sense_hat_csv.GYRO
            break
        else:
            print("Invalid choice, please try again...")

    inputDeviceId = input("Please enter a device ID: ")
    sensor_location = input("Where is the IMU located? ")
    exercise = input("Please enter the exercise being recorded: ")
    subject = input("Who is wearing the IMU? ")

    config = {
        'experimentId': experiment_id,
        'type': sensor_type,
        'sensorLocation': sensor_location,
        'subject': subject,
        'exercise': exercise,
        'isRaw': False,
        'timestamp': round(time.time() * 1000),
        'deviceId': inputDeviceId
    }

    filename = config['experimentId'] + "-" + config['timestamp'] + ".csv"
    with open(filename, 'a') as file:
        while True:
            x = sense_hat_csv.get_record_from_radians().get('xRoll')
            y = sense_hat_csv.get_record_from_radians().get('yPitch')
            z =  sense_hat_csv.get_record_from_radians().get('zYaw')
            exp_id = sense_hat_csv.get_record_from_radians().get('experimentId')
            exercise = sense_hat_csv.get_record_from_radians().get('exercise')

            file.write(f"{x},{y},{z}")


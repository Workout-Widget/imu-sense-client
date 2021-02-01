# IMU REST Client for the SenseHAT
## Overview
This is a simply Python script that reads data from the SenseHAT IMU and sends the data via REST calls to a server endpoint. The server is a minimalist REST API for R&D purposes only. The server can be found here: https://github.com/Workout-Widget/imu-rest-go
## How To Run
There are two scripts in the `src/` directory. One is a test script for debugging, `mock-rest-client.py`, and the other is the actual IMU REST client: `imu-radians-rest.py`. 

First open `imu-radians-rest.py`

In the line `rest_endpoint = "http://REST_SERVER_IP:8080/motion/"` replace _REST_SERVER_IP_ placeholder to the IP of the Go REST API.

Ensure that your Raspberry Pi has the SenseHAT Python library installed.
```
sudo apt-get update && sudo apt-get install sense-hat
```
Now, you can simply run the mock-rest-client.py script and it will begin sending data to the server.

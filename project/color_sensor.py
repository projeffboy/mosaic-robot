#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
Based on collect_us_sensor_data.py
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor
from time import sleep


# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(4)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
class Color:
    def collect_color_sensor_data():
        "Collect color sensor data."
        print("Starting to collect color samples")
        
        while True: # poll for press
            print("Not enough cubes")
            count = 0
            rgb_values = COLOR_SENSOR.get_color_name() # get r, g, b as a list
            print(rgb_values)
            sleep(1) # delay seconds
            if (rgb_values != "Unknown"):
                return True
                


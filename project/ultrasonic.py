#!/usr/bin/env python3

"""
Module to play drums when the motor senses the right angle.
This file must be run on the robot.
"""
import brickpi3
from utils.brick import wait_ready_sensors
from time import sleep
from utils.sound import Sound


class Ultrasonic:
    def get_us_sensor():
        Note1 = Sound(duration=0.1, volume=96, pitch="C3")
        Note2 = Sound(duration=0.1, volume=96, pitch="D3")
        Note3 = Sound(duration=0.1, volume=96, pitch="E3")
        
        BP = brickpi3.BrickPi3()
        US_SENSOR = BP.PORT_4
        BP.set_sensor_type(US_SENSOR, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

        wait_ready_sensors() # Note: Touch sensors actually have no initialization time
        
        print("US sensor initialized.")
        count = 0
        while(True):
            print("Polling.")
            # poll for button press
            distance = BP.get_sensor(US_SENSOR)
            print(distance)
            sleep(0.5)
            if (distance < 4.5):
                count += 1
            if (distance > 250):
                BP.set_sensor_type(US_SENSOR, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
                wait_ready_sensors()
                count = 0
            if count >= 5:
                Note2.play()
                Note2.wait_done()
                Note1.play()
                Note1.wait_done()
                Note3.play()
                Note3.wait_done()
                return True
#!/usr/bin/env python3

"""
Module to play drums when the motor senses the right angle.
This file must be run on the robot.
"""
from utils.brick import EV3UltrasonicSensor, wait_ready_sensors
from time import sleep
from sound import Sound, DummySound

class Ultrasonic:
    def __init__(
        self,
        port,
        polling_period=0.5,
        sound=False,
        async_sound=False,
        debug=False,
    ):
        self.sensor = EV3UltrasonicSensor(port)
        self.polling_period = polling_period
        self.sound = sound
        self.debug = debug

        self.sound = DummySound()
        if sound:
            self.sound = Sound(asynchronous=async_sound)
    
    def detect_full_tower(self):
        self.sound.play("insert")

        wait_ready_sensors(True)
        
        detected_count = 0
        while True:
            distance = self.sensor.get_value()
            if self.debug:
                print(distance)
            if distance < 4.5:
                detected_count += 1
            elif distance < 250:
                detected_count = 0
            else:
                wait_ready_sensors(True)
                detected_count = 0
            if detected_count >= 5:
                self.sound.play("tower_full", must_be_sync=True)
                
                break
            sleep(self.polling_period)
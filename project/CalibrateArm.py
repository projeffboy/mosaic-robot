#!/usr/bin/env python3

"""
Run this file to run the robot
"""
 
from utils.brick import Motor
from time import sleep
from utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR1 = TouchSensor(1)
TOUCH_SENSOR2 = TouchSensor(2)

#left motor
motor1 = Motor("A")
#right motor
motor2 = Motor("B")

# CONFIGS

init_D_x = 8.8
radius_big = 2.1
pixel_width = 4
pixel_height = 4
pi = 3.14159264
num_col = 5
num_row = 5

def piston_x_axis(pixel_slot):
    init_distance = init_D_x
    if (pixel_slot < 1 or pixel_slot > num_col):
        print(pixel_slot + " is an invalid pixel column slot.")
        exit()
    try:
        pushing_distance = init_distance + ((pixel_slot) * pixel_width)
        rotation_in_degrees = (360 * pushing_distance)/(2*pi*radius_big)
        move_piston(rotation_in_degrees)
    except BaseException:
        print(BaseException)
        exit()

def move_piston(rotation_in_degrees):
    try:
        motor1.set_position_relative(-rotation_in_degrees)
        motor2.set_position_relative(-rotation_in_degrees)
        sleep(2)
        motor1.set_position_relative(rotation_in_degrees)
        motor2.set_position_relative(rotation_in_degrees)
        sleep(2)
    except BaseException:
        print(BaseException)
        exit()

if __name__=='__main__':
    drawing = input("Please enter the array of 1s and 0s for the canvas:")
    
    reversedInput = drawing[::-1]
    slot_counter = num_col
    # TODO remove output string and all printings once testing is complete
    for binary in reversedInput:
        if binary == "1":
            piston_x_axis(slot_counter)
            slot_counter -= 1
        else:
            slot_counter -= 1
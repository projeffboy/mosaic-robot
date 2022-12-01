#!/usr/bin/env python3

"""
Run this file to run the robot
"""
 
from utils.brick import Motor
from time import sleep
from utils.brick import TouchSensor

TOUCH_SENSOR1 = TouchSensor(1)
TOUCH_SENSOR2 = TouchSensor(2)

#motors
motor1 = Motor("A")
#motor1.set_limits(dps=360)
# motor2 = Motor("B")
#motor2.set_limits(dps=360)

# CONFIGS
init_D_x = 9
radius_big = 2.1
pixel_width = 4
pixel_height = 4
pi = 3.14159264
num_col = 5
num_row = 5

def piston_x_axis(pixel_slot):
    if (pixel_slot < 1 or pixel_slot > num_col):
        print(pixel_slot + " is an invalid pixel column slot.")
        exit()
    
    init_distance = init_D_x
    try:
        pushing_distance = init_distance + pixel_slot * pixel_width
        rotation_in_degrees = (360 * pushing_distance) / (2 * pi * radius_big)
        move_piston(rotation_in_degrees)
    except BaseException:
        print(BaseException)
        exit()

def move_piston(rotation_in_degrees):
    try:
        motor1.set_position_relative(-rotation_in_degrees)
        # motor2.set_position_relative(-rotation_in_degrees)
        sleep(1.5)
        motor1.set_position_relative(rotation_in_degrees)
        # motor2.set_position_relative(rotation_in_degrees)
        sleep(1.5)
    except BaseException:
        print(BaseException)
        exit()

if __name__=='__main__':
    drawing = input("Please enter up to five 1s and 0s for the canvas:")
    binary = drawing[:5] # if you push from the right you don't need to reverse
    # drawing[4::-1] # get the first 5 input and reverse it
    slot_counter = num_col

    for bit in binary:
        if bit == "1":
            piston_x_axis(slot_counter)
        slot_counter -= 1
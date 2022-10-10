#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils.brick import Motor
from time import sleep
from utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR1 = TouchSensor(1)
TOUCH_SENSOR2 = TouchSensor(2)

# motor1 = Motor("A")
# motor2 = Motor("B")

# CONFIGS

init_D_x = 10
init_D_y = 0.75
radius_big = 1.85
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
        pushing_distance = init_distance + ((pixel_slot - 1) * pixel_width)
        rotation_in_degrees = (360 * pushing_distance)/(2*pi*radius_big)
        # TODO : remove the print once testing is complete
        return rotation_in_degrees
        # move_piston(rotation_in_degrees)
    except BaseException:
        print(BaseException)
        exit()

def piston_y_axis(pixel_slot):
    init_distance = init_D_y
    if (pixel_slot < 1 or pixel_slot > num_row):
        print(pixel_slot + " is an invalid pixel row slot.")
        exit()
    try:
        pushing_distance = init_distance + ((pixel_slot - 1) * pixel_height)
        rotation_in_degrees = (360 * pushing_distance)/(2*pi*radius_big)
        # TODO : remove the print once testing is complete
        return rotation_in_degrees
        # move_piston(rotation_in_degrees)
    except BaseException:
        print(BaseException)
        exit()

# def move_piston(rotation_in_degrees):
#     try:
#         motor1.set_position(rotation_in_degrees)
#         motor2.set_position(rotation_in_degrees)
#         sleep(2)
#         motor1.set_position(-rotation_in_degrees)
#         motor2.set_position(-rotation_in_degrees)
#         sleep(2)
#     except BaseException:
#         exit()

if __name__=='__main__':
    drawing = input("Please enter the array of 1s and 0s for the canvas:")
    
    reversedInput = drawing[::-1]
    slot_counter = num_col
    row_counter = num_row
    # TODO remove output string and all printings once testing is complete
    outputString = ""
    for binary in reversedInput:
        if binary == "1":
            outputString += str(piston_x_axis(slot_counter)) + " "
            # outputString = outputString + "1"
        else:
            outputString += "0 "
        if slot_counter == 1:
            slot_counter = 6
            outputString = outputString + " ||  row push-angle: " + str(piston_y_axis(row_counter))
            row_counter -= 1
            print(outputString)
            outputString = ""
        slot_counter -= 1
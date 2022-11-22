#!/usr/bin/env python3

"""
Run this file to run the robot
"""
 
from utils.brick import Motor
from time import sleep
from utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR1 = TouchSensor(1)
TOUCH_SENSOR2 = TouchSensor(2)


motor1 = Motor("A")
motor2 = Motor("D")

# CONFIGS
init_D_y = 3
init_D_x = 16
radius_big = 2.1
pixel_width = 4
pixel_height = 4
pi = 3.14159264
num_col = 5
num_row = 5
num_pixels = num_col * num_row

def piston_x_axis(pixel_slot):
    init_distance = init_D_x
    if (pixel_slot < 0 or pixel_slot > num_col):
        print(pixel_slot + " is an invalid pixel column slot.")
        exit()
    try:
        #pushing_distance = init_distance + ((pixel_slot) * pixel_width)
        #rotation_in_degrees = (360 * pushing_distance)/(2*pi*radius_big)
        if (pixel_slot == 0):
            rotation_in_degrees = 436
        elif (pixel_slot == 1):
            rotation_in_degrees = 545
        elif (pixel_slot == 2):
            rotation_in_degrees = 654
        elif (pixel_slot == 3):
            rotation_in_degrees = 763
        elif (pixel_slot == 4):
            rotation_in_degrees = 872
        else :
            print("Incorrect index for col.")
            exit()
        move_piston(rotation_in_degrees, motor1)
    except BaseException as e:
        print(e)
        exit()

def piston_y_axis(row_slot):
    init_distance = init_D_y
    #if (row_slot < 0 or row_slot >= num_row):
        #print(str(row_slot) + " is an invalid pixel row slot.")
        #exit()
    try:
        #pushing_distance = init_distance + ((row_slot) * pixel_width)
        #rotation_in_degrees = (360 * pushing_distance)/(2*pi*radius_big)
        if (row_slot == 0):
            rotation_in_degrees = 84
        elif (row_slot == 1):
            rotation_in_degrees = 193
        elif (row_slot == 2):
            rotation_in_degrees = 302
        elif (row_slot == 3):
            rotation_in_degrees = 411
        elif (row_slot == 4):
            rotation_in_degrees = 520
        else :
            print("Incorrect index for col.")
            exit()
        move_piston(rotation_in_degrees, motor2)
    except BaseException as e:
        print(e)
        exit()

def move_piston(rotation_in_degrees, aMotor):
    motor = aMotor
    try:
        motor.set_limits(power = 50, dps = 800)
        sleep(1)
        motor.set_position(-rotation_in_degrees)
        sleep(3)
        motor.set_position(0)
        sleep(3)
    except BaseException as e:
        print(e)
        exit()

if __name__=='__main__':
    drawing = ""
    motor1.offset_encoder(0)
    motor2.offset_encoder(0)
    while True:
        if (len(drawing) > num_pixels):
            break
        if (TOUCH_SENSOR1.is_pressed() and TOUCH_SENSOR2.is_pressed()):
            sleep(0.5)
            drawing = input("Please enter the array of 1s and 0s for the canvas:")
            break
        if (TOUCH_SENSOR1.is_pressed() and not TOUCH_SENSOR2.is_pressed()):
            sleep(0.5)
            drawing += '1'
            print(drawing)
        if (not TOUCH_SENSOR1.is_pressed() and TOUCH_SENSOR2.is_pressed()):
            sleep(0.5)
            drawing += '0'
            print(drawing)
    number_of_cubes = drawing.count('1')
    if number_of_cubes > 15: 
        raise Exception("Maximum number of cubes is 15. Please try again")
    reversedInput = drawing[::-1]
    slot_counter = num_col - 1
    row_counter = num_row - 1
    for binary in reversedInput:
        if binary == "1":
            piston_x_axis(slot_counter)
        if binary == "0":
            num_row -= 1
        if slot_counter == 0:
            slot_counter = num_col
            piston_y_axis(row_counter)
            row_counter -= 1
        slot_counter -= 1
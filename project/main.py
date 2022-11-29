#!/usr/bin/env python3

"""
Run this file to run the robot
"""
 
from utils.brick import Motor
from time import sleep
from utils.brick import TouchSensor, wait_ready_sensors
from button_input import button_input

# INIT I/O
DRAW_0_BTN = TouchSensor(1)
DRAW_1_BTN = TouchSensor(2)
PUSHER = Motor("A")
SWEEPER = Motor("D")
wait_ready_sensors(True) # set to True to print out helpful stuff
PUSHER.offset_encoder(0)
SWEEPER.offset_encoder(0)

# CONFIG
BTN_POLLING_PERIOD = 0.5
INIT_D_Y = 3
INIT_D_X = 16
RADIUS_BIG = 2.1
PIXEL_WIDTH_CM = 4
PIXEL_HEIGHT_CM = 4
PI = 3.14159264
NUM_COL = 5
NUM_ROW = 5
NUM_PIXELS = NUM_COL * NUM_ROW

def piston_x_axis(pixel_slot):
    init_distance = INIT_D_X
    if (pixel_slot < 0 or pixel_slot > NUM_COL):
        print(pixel_slot + " is an invalid pixel column slot.")
        exit()
    try:
        # pushing_distance = init_distance + ((pixel_slot) * PIXEL_WIDTH_CM)
        # rotation_in_degrees = (360 * pushing_distance)/(2*PI*RADIUS_BIG)
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
        move_piston(rotation_in_degrees, PUSHER)
    except BaseException as e:
        print(e)
        exit()

def piston_y_axis(row_slot):
    init_distance = INIT_D_Y
    #if (row_slot < 0 or row_slot >= num_row):
        #print(str(row_slot) + " is an invalid pixel row slot.")
        #exit()
    try:
        #pushing_distance = init_distance + ((row_slot) * pixel_width)
        #rotation_in_degrees = (360 * pushing_distance)/(2*PI*RADIUS_BIG)
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
        move_piston(rotation_in_degrees, SWEEPER)
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

if __name__=="__main__":
    drawing = button_input(
        DRAW_0_BTN,
        DRAW_1_BTN,
        NUM_PIXELS,
        reverse_drawing=True,
        polling_rate=BTN_POLLING_PERIOD,
    )
    binary = { "0", "1"}
    characters = set(drawing)
    if not (binary == characters or characters == {'0'} or characters == {'1'}) or len(input) > 25:
        print("Incorrect input: input must be binary and a size of 25.")
    col_counter = NUM_COL - 1
    row_counter = NUM_ROW - 1
    for binary in drawing:
        if binary == "1":
            piston_x_axis(col_counter)
        elif binary == "0":
            NUM_ROW -= 1
        else:
            print("Something unexpected happened.")

        if col_counter == 0:
            col_counter = NUM_COL
            piston_y_axis(row_counter)
            row_counter -= 1

        col_counter -= 1
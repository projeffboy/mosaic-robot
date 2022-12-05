#!/usr/bin/python3

"""
Run this file to run the robot
NOTE:
The pusher and cube tower have to be pushing from the right side of the canvas. If you want it to push from the left, set reverse_rows=True
The sweeper has to be sweeping from the bottom side. If you want it to push from the right, set reverse_each_row=True.

Use this file for the acceptance and nonfunctional tests
"""
from button_input import ButtonInput
from arms import Arms
from ultrasonic import Ultrasonic

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2
UNDO_BTN_PORT = 3
ULTRASONIC_PORT = 4
PUSHER_PORT = "A"
START_PORT = "C"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

if __name__=="__main__":

    # 1. Draw
    btnInput = ButtonInput(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        UNDO_BTN_PORT,
        START_PORT,
        NUM_COLS,
        NUM_ROWS,
        reverse_each_row=True,
        reverse_rows=True,
        sound=True,
        async_sound=True,
        debug=True,
    )
    drawing = btnInput.input_drawing()
    # 2. Put cubes in
    ultrasonic = Ultrasonic(
        ULTRASONIC_PORT, sound=True, async_sound=True, debug=True
    )
    ultrasonic.detect_full_tower()
    # 3. Draw
    arms = Arms(
        PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS, sound=True
    )
    arms.draw()

#!/usr/bin/python3

"""
Run this file to run the robot
NOTE:
The pusher and cube tower have to be pushing from the right side of the canvas. If you want it to push from the left, set reverse_col=True
The sweeper has to be sweeping from the bottom side. If you want it to push from the right, set reverse_row=True.
"""
from button_input import ButtonInput
from arms import Arms
from ultrasonic import Ultrasonic

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2
START_BTN_PORT = 3
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

if __name__=="__main__":
    # 1. Draw
    btnInput = ButtonInput(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        START_BTN_PORT,
        NUM_COLS,
        NUM_ROWS,
        reverse_col=True,
        reverse_row=True,
        sound=True,
        debug=True,
    )
    drawing = btnInput.input_drawing()
    # 2. Put cubes in
    all_cubes_in = Ultrasonic.get_us_sensor()
    if all_cubes_in:
        print("15 cubes in.")
    # 3. Draw
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS)
    arms.draw()

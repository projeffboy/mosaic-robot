#!/usr/bin/python3

"""
Run this file to run the robot
NOTE: The pusher and cube tower have to be pushing from the left side of the canvas.
The sweeper has to be sweeping from the bottom side.
"""
from button_input import ButtonInput
from arms import Arms
from ultrasonic import Ultrasonic

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2
DRAW_REST_BTN_PORT = 3
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

if __name__=="__main__":
    all_cubes = Ultrasonic.get_us_sensor()
    if (all_cubes) :
        print("15 cubes in.")
    btnInput = ButtonInput(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        DRAW_REST_BTN_PORT,
        NUM_COLS,
        NUM_ROWS,
        reverse_col=True,
        debug=True,
    )
    
    drawing = btnInput.input_drawing()
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS)
    arms.draw()

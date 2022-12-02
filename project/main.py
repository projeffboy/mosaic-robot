#!/usr/bin/python3

"""
Run this file to run the robot
NOTE: The pusher and cube tower have to be pushing from the left side of the canvas.
The sweeper has to be sweeping from the bottom side.
"""

# SOFTWARE SUBSYSTEMS (go to these files to check the I/O config)
from button_input import input_drawing
from arms import Arms

# I/O PORTS
PUSHER_PORT = "A"
SWEEPER_PORT = "D"
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2

# CONFIG/CONSTANTS
NUM_COL = 5
NUM_ROW = 5

if __name__=="__main__":
    drawing = input_drawing(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        NUM_COL,
        NUM_ROW,
        reverse_col=True,
        debug=True
    )
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COL, NUM_ROW)
    arms.draw()

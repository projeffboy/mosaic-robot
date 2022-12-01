#!/usr/bin/env python3

"""
Run this file to run the robot
"""

# SOFTWARE SUBSYSTEMS (go to these files to check the I/O config)
from button_input import input_drawing
from arms import Arms

# CONFIG/CONSTANTS
NUM_COL = 5
NUM_ROW = 5
NUM_PIXELS = NUM_COL * NUM_ROW

if __name__=="__main__":
    drawing = input_drawing(NUM_PIXELS, reverse_drawing=True, debug=True)
    arms = Arms(drawing, NUM_COL, NUM_ROW)
    arms.draw()

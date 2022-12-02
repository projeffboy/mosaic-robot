#!/usr/bin/python3

"""
Test the button input component
"""

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from button_input import ButtonInput

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

btnInput = ButtonInput(
    DRAW_0_BTN_PORT,
    DRAW_1_BTN_PORT,
    NUM_COLS,
    NUM_ROWS,
    reverse_col=True,
    debug=True,
)
drawing = btnInput.input_drawing()
print("TEST OUTPUT:", drawing)
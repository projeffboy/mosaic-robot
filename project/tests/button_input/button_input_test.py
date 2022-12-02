#!/usr/bin/python3

"""
Test the button input component
"""

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from button_input import input_drawing

# CONFIG/CONSTANTS
NUM_COL = 5
NUM_ROW = 5
NUM_PIXELS = NUM_COL * NUM_ROW

drawing = input_drawing(NUM_PIXELS, reverse_drawing=True, debug=True)
print("TEST OUTPUT:", drawing)
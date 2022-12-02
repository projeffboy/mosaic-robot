#!/usr/bin/python3

"""
Test pushing a row of cubes
"""

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from arms import Arms

# I/O PORTS
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5
NUM_PIXELS = NUM_COLS * NUM_ROWS

if __name__=="__main__":
    drawing = "1111100000111110000011111"
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS)
    arms.draw()

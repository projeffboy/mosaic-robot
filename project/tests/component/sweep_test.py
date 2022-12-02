#!/usr/bin/python3

"""
Test pushing one cube
"""

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from arms import Arms

# I/O PORTS
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COL = 5
NUM_ROW = 5
NUM_PIXELS = NUM_COL * NUM_ROW

if __name__=="__main__":
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, "", NUM_COL, NUM_ROW)
    arms.piston_y_axis(4)

#!/usr/bin/python3

"""
Test the pusher and sweeper component
"""

# SOFTWARE SUBSYSTEMS (go to these files to check the I/O config)
from button_input import input_drawing
from arms import Arms

# I/O PORTS
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COL = 5
NUM_ROW = 5
NUM_PIXELS = NUM_COL * NUM_ROW

if __name__=="__main__":
    drawing = "0000000000000000001111111"
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COL, NUM_ROW)
    arms.draw()

#!/usr/bin/python3

# Commponents involved: sweeper

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from button_input import ButtonInput
from arms import Arms

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2
PUSHER_PORT = "A"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

if __name__=="__main__":
    btnInput = ButtonInput(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        NUM_COLS,
        NUM_ROWS,
        reverse_col=True,
        debug=True,
    )
    drawing = btnInput.input_drawing()
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS)
    arms.draw()

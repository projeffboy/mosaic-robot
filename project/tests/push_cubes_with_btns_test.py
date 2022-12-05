#!/usr/bin/python3

# Commponents involved: sweeper

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from button_input import ButtonInput
from arms import Arms

# I/O PORTS
DRAW_0_BTN_PORT = 1
DRAW_1_BTN_PORT = 2
UNDO_BTN_PORT = 3
PUSHER_PORT = "A"
START_PORT = "C"
SWEEPER_PORT = "D"

# CONFIG/CONSTANTS
NUM_COLS = 5
NUM_ROWS = 5

if __name__=="__main__":
    btnInput = ButtonInput(
        DRAW_0_BTN_PORT,
        DRAW_1_BTN_PORT,
        UNDO_BTN_PORT,
        START_PORT,
        NUM_COLS,
        NUM_ROWS,
        reverse_each_row=True,
        reverse_rows=True,
    )
    drawing = btnInput.input_drawing()
    arms = Arms(PUSHER_PORT, SWEEPER_PORT, drawing, NUM_COLS, NUM_ROWS)
    arms.draw()

"""
Button Input Component

- three buttons and one motor
- motor is up
    - S1: draw 0
    - S2: draw 1
    - S3: start
    - S1&2: terminal input
- motor is down
    - S1: undo
    - S2: restart drawing (even while drawing)
"""

from time import sleep
from utils.brick import TouchSensor, wait_ready_sensors

# CONFIG/CONSTANTS
DRAW_0_BTN = TouchSensor(1)
DRAW_1_BTN = TouchSensor(2)
POLLING_PERIOD = 0.5

wait_ready_sensors(True) # set to True to print out helpful stuff

def input_drawing(num_pixels, reverse_drawing=False, debug=False):
    drawing = ""

    while True:
        pressed = True
        if len(drawing) > num_pixels:
            break
        elif DRAW_0_BTN.is_pressed() and DRAW_1_BTN.is_pressed():
            while True:
                drawing = input(
                    "Please enter the array of 1s and 0s for the canvas:"
                )
                if debug:
                    print(drawing)
                if set(drawing).issubset({'0', '1'}): # check that only 1s and 0s
                    drawing = drawing.ljust(20, "0")
                    break
                else:
                    print("Invalid input.")
            break
        elif DRAW_0_BTN.is_pressed() and not DRAW_1_BTN.is_pressed():
            drawing += "1"
        elif DRAW_1_BTN.is_pressed():
            drawing += "0"
        else:
            pressed = False
        
        sleep(POLLING_PERIOD)
        if debug and pressed:
            print(drawing)


    number_of_cubes = drawing.count("1")
    if number_of_cubes > 15:
        raise Exception("Maximum number of cubes is 15. Please try again")

    if reverse_drawing:
        drawing = drawing[::-1]
    
    return drawing
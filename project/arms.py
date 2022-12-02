"""
Pusher and sweeper components
"""

from time import sleep
from utils.brick import Motor

class Arms():
    # CONFIG/CONSTANTS
    INIT_D_Y = 3
    INIT_D_X = 16
    RADIUS_BIG = 2.1
    PIXEL_WIDTH_CM = 4
    PIXEL_HEIGHT_CM = 4
    PI = 3.14159264

    def __init__(self, pusher_port, sweeper_port, drawing, num_col, num_row):
        self.drawing = drawing
        self.num_col = num_col
        self.num_row = num_row

        # INIT I/O
        self.pusher = Motor(pusher_port)
        self.sweeper = Motor(sweeper_port)
        self.pusher.offset_encoder(0)
        self.sweeper.offset_encoder(0)

    def draw(self):
        col = self.num_col - 1
        row = self.num_row - 1
        for binary in self.drawing:
            if binary == "1":
                self.__piston_x_axis(col)
            elif binary != "0":
                print("Something unexpected happened.")

            if col == 0:
                col = self.num_col
                self.__piston_y_axis(row)
                row -= 1

            col -= 1

    def __piston_x_axis(self, col):
        if (col < 0 or col > self.num_col):
            print(col + " is an invalid column slot.")
            exit()

        try:
            rotations_in_deg = [436, 545, 654, 763, 872]
            rotation_in_deg = rotations_in_deg[col]
            self.__move_piston(rotation_in_deg, self.pusher)
            # init_distance = INIT_D_X
            # pushing_distance = init_distance + ((col_slot) * PIXEL_WIDTH_CM)
            # rotation_in_degrees = (360 * pushing_distance)/(2*PI*RADIUS_BIG)
        except BaseException as e:
            print(e)
            exit()

    def __piston_y_axis(self, row):
        if (row < 0 or row >= self.NUM_ROW):
            print(str(row) + " is an invalid row slot.")
            exit()

        try:
            rotations_in_deg = [84, 193, 302, 411, 520]
            rotation_in_deg = rotations_in_deg[row]

            self.__move_piston(rotation_in_deg, self.sweeper)
            # init_distance = INIT_D_Y
            #pushing_distance = init_distance + ((row_slot) * pixel_width)
            #rotation_in_degrees = (360 * pushing_distance)/(2*PI*RADIUS_BIG)
        except BaseException as e:
            print(e)
            exit()

    def __move_piston(self, rotation_in_degrees, motor):
        try:
            motor.set_limits(power = 50, dps = 800)
            sleep(1)
            motor.set_position(-rotation_in_degrees)
            sleep(3)
            motor.set_position(0)
            sleep(3)
        except BaseException as e:
            print(e)
            exit()
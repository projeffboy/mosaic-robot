"""
Pusher and sweeper components
"""

from time import sleep
from utils.brick import Motor
from sound import Sound, DummySound

class Arms():
    def __init__(
        self,
        pusher_port,
        sweeper_port,
        drawing,
        num_col,
        num_row,
        sound = False
    ):
        self.drawing = drawing
        self.num_col = num_col
        self.num_row = num_row
        self.cube_count = 0
        self.sound = DummySound()
        if sound:
            self.sound = Sound()
        
        # INIT I/O
        self.pusher = Motor(pusher_port)
        self.sweeper = Motor(sweeper_port)
        self.pusher.offset_encoder(0)
        self.sweeper.offset_encoder(0)

    def draw(self):
        col = self.num_col - 1
        row = self.num_row - 1
        empty_row = True
        for binary in self.drawing:
            if binary == "1":
                self.piston_x_axis(col)
                empty_row = False
            elif binary != "0":
                print("Something unexpected happened.")

            if col == 0:
                col = self.num_col
                if not empty_row:
                    self.piston_y_axis(row)
                empty_row = True
                row -= 1

            col -= 1
        self.sound.play("complete")

    def piston_x_axis(self, col):
        if (col < 0 or col > self.num_col):
            print(col + " is an invalid column slot.")
            exit()

        try:
            #rotations_in_deg = [436, 545, 654, 763, 872]
            rotations_in_deg = [325, 436, 545, 654, 755]
            rotation_in_deg = rotations_in_deg[col] - (self.cube_count)
            self.__move_piston(rotation_in_deg, self.pusher)
            self.cube_count += 1
        except BaseException as e:
            print(e)
            exit()

    def piston_y_axis(self, row):
        if (row < 0 or row >= self.num_row):
            print(str(row) + " is an invalid row slot.")
            exit()

        try:
            rotations_in_deg = [0, 193, 302, 411, 520]
            rotation_in_deg = rotations_in_deg[row]

            self.__move_piston(rotation_in_deg, self.sweeper)
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
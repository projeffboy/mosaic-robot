"""
Button Input Component

- three buttons S1,2,3
    - S1: draw 0
    - S2: draw 1
    - S3: undo
    - S1&2: terminal input
- one motor M
    - move motor 90 deg clockwise or counterclockwise: finish drawing
"""

from time import sleep
from utils.brick import TouchSensor, Motor, wait_ready_sensors
from sound import Sound, DummySound

class ButtonInput:
    def __init__(
        self,
        draw_0_btn_port,
        draw_1_btn_port,
        undo_btn_port,
        start_port,
        num_cols,
        num_rows,
        reverse_rows=True,
        reverse_each_row=True,
        polling_period=0.1,
        max_blocks=15,
        sound=False,
        async_sound=False,
        debug=False,
    ):
        # INIT I/O
        self.draw_0_btn = TouchSensor(draw_0_btn_port)
        self.draw_1_btn = TouchSensor(draw_1_btn_port)
        self.undo_btn = TouchSensor(undo_btn_port)
        self.start = Motor(start_port)
        wait_ready_sensors(True) # True to print out debug stuff
        self.is_pressed = {
            "draw_0_btn": {
                "btn": self.draw_0_btn,
                "is_pressed": False,
            },
            "draw_1_btn": {
                "btn": self.draw_1_btn,
                "is_pressed": False,
            },
            "undo_btn": {
                "btn": self.undo_btn,
                "is_pressed": False,
            }
        }
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.reverse_each_row = reverse_each_row
        self.reverse_rows = reverse_rows
        self.debug = debug
        self.polling_period = polling_period
        self.max_blocks = max_blocks

        self.drawing = ""

        self.sound = DummySound()
        if sound:
            self.sound = Sound(asynchronous=async_sound)


    def input_drawing(self):
        self.sound.play("welcome")
        init_pos = self.start.get_position()

        while True:
            pressed = True
            draw_0 = self.__is_just_pressed("draw_0_btn")
            draw_1 = self.__is_just_pressed("draw_1_btn")
            undo = self.__is_just_pressed("undo_btn")
            if self.__finished():
                self.sound.play("fifteen_pixels", must_be_sync=True)
                break
            elif draw_0 and draw_1:
                self.sound.play("terminal")
                self.__terminal_input()
                break
            elif not draw_0 and draw_1:
                self.drawing += "1"
                self.sound.play("one", must_be_sync=self.__finished())
            elif draw_0:
                self.drawing += "0"
                self.sound.play("zero", must_be_sync=self.__finished())
            elif abs(init_pos - self.start.get_position()) > 45:
                while (len(self.drawing) < self.__num_pixels()):
                    self.drawing += "0"
                self.sound.play("fill_in", must_be_sync=True)
                break
            elif undo:
                self.drawing = self.drawing[:-1]
                self.sound.play("undo")
            else:
                pressed = False
            
            sleep(self.polling_period)
            if self.debug and pressed:
                print(self.drawing)
        self.sound.play("drawing_received", must_be_sync=True)

        if self.__too_much_blocks():
            raise Exception("Maximum number of cubes is 15. Please try again")

        if self.reverse_each_row:
            drawing_arr = list(self.drawing)
            for row in range(self.num_rows):
                start = row * self.num_cols
                end = start + self.num_cols
                row_pixels = drawing_arr[start:end]
                row_pixels.reverse()
                drawing_arr[start:end] = row_pixels
            self.drawing = "".join(drawing_arr)
        
        if self.reverse_rows:
            output = ""
            for row in range(self.num_rows):
                start = row * self.num_cols
                end = start + self.num_cols
                output = self.drawing[start:end] + output
            self.drawing = output
        
        return self.drawing

    def __finished(self):
        return self.__reached_max_blocks() or len(self.drawing) >= self.__num_pixels()

    def __is_just_pressed(self, btnName):
        btn = self.is_pressed[btnName]["btn"]
        is_pressed_old = self.is_pressed[btnName]["is_pressed"]
        is_pressed = btn.is_pressed()
        output = is_pressed and not is_pressed_old
        self.is_pressed[btnName]["is_pressed"] = is_pressed
        return output

    def __reached_max_blocks(self):
        number_of_cubes = self.drawing.count("1")
        return number_of_cubes == self.max_blocks

    def __too_much_blocks(self):
        number_of_cubes = self.drawing.count("1")
        return number_of_cubes > self.max_blocks


    def __terminal_input(self):
        print("(starting from 1st row, 1st column, going left to right, then top to bottom)")
        while True:
            self.drawing = input(
                "Please enter a string of 1s and 0s for the canvas:"
            )
            if self.debug:
                print(self.drawing)
            # check 1
            if set(self.drawing).issubset({'0', '1'}): # check that only 1s and 0s
                self.drawing = self.drawing.ljust(self.__num_pixels(), "0")
            else:
                print("Invalid input.")
                continue
            # check 2
            if len(self.drawing) > self.__num_pixels():
                print("Your string is too long")
                continue
            #  check 3
            if self.__too_much_blocks():
                self.__too_much_blocks_msg()
                continue
            else:
                break

    def __num_pixels(self):
        return self.num_rows * self.num_cols

    def __too_much_blocks_msg(self):
        print(f"You can only draw with up to {self.max_blocks} blocks, try again.")
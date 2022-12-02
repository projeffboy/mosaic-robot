#!/usr/bin/python3

# Component: Sound

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from sound import Sound

sound = Sound()
sound.play("welcome")
sound.play("zero")
sound.play("one")
sound.play("undo")
sound.play("start_over")
sound.play("terminal")
sound.play("fifteen_pixels")
sound.play("drawing_received")
sound.play("tower_full")
sound.play("fill_in")
sound.play("insert")
sound.play("complete")
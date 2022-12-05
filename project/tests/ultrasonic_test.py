import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from ultrasonic import Ultrasonic

ULTRASONIC_PORT = 4

ultrasonic = Ultrasonic(ULTRASONIC_PORT, debug=True)
ultrasonic.detect_full_tower()
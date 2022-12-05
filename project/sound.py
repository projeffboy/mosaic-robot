"""
Plays audio from the sibling `sound` folder.
"""

from os.path import dirname, join, abspath
import simpleaudio as sa

class Sound:
    def __init__(self, asynchronous=False):
        self.asynchronous = asynchronous

    def play(self, file_base_name, must_be_sync=False):
        path = self.__get_path(file_base_name)
        wave_obj = sa.WaveObject.from_wave_file(path)
        play_obj = wave_obj.play()
        if not self.asynchronous or must_be_sync:
            play_obj.wait_done()

    def __get_path(self, file_base_name):
        sound_dir_path = abspath(
            join(dirname(__file__), "sound", file_base_name + ".wav")
        )

        return sound_dir_path

class DummySound():
    def play(self, *args, **kwargs):
        pass
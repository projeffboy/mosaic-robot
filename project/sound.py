"""
Plays audio from the sibling `sound` folder.
"""

from os.path import dirname, join, abspath
import simpleaudio as sa

class Sound:
    def play(self, file_base_name):
        path = self.__get_path(file_base_name)
        wave_obj = sa.WaveObject.from_wave_file(path)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def __get_path(self, file_base_name):
        sound_dir_path = abspath(
            join(dirname(__file__), "sound", file_base_name + ".wav")
        )

        return sound_dir_path
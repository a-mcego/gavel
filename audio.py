import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()

def play_file(filename, block=True):
    mixer.music.load(filename)
    mixer.music.play()
    if block:
        while mixer.music.get_busy():
            pass

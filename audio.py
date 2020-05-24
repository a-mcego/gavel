import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer # type: ignore
import threading
mixer.init()

currently_playing = None
stop_called = False

def play_file_thread(filename):
    global currently_playing
    global stop_called
    if type(filename) == str:
        currently_playing = filename
        mixer.music.load(filename)
        mixer.music.play()
        while mixer.music.get_busy():
            if stop_called:
                mixer.music.stop()
                break
            pass
    elif type(filename) == list:
        for fn in filename:
            play_file_thread(fn)
    currently_playing = None

#filename can be either str or List[str]
def play_file(filename, block=False):
    stop_called = False
    t = threading.Thread(target=play_file_thread, args=(filename,))
    t.start()

def stop():
    global stop_called
    stop_called = True

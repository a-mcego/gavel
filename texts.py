import random
import os
import pathlib

import audio

class Sentence:
    def __init__(self, mp3name, txtname):
        self.mp3name = mp3name
        self.txtname = txtname

    def get_translations(self):
        ret = []
        with open(self.txtname) as txtfile:
            ret.append(txtfile.readline())
            ret.append(txtfile.readline())
        return ret

    def play_audio(self):
        audio.play_file(self.mp3name)

class Text:
    def __init__(self, path):
        self.path = path
        self.description = path #TODO: add a proper description file
        self.sentences = []
        for path in pathlib.Path(self.path).rglob('*.mp3'):
            mp3name = os.path.join(self.path,path.name)
            txtname = mp3name[:-4] + ".txt"
            if not os.path.exists(txtname):
                #print(f"No text for {mp3name}")
                continue
            self.sentences.append(Sentence(mp3name,txtname))
        print(f"{len(self.sentences)} sentences loaded with text.")

    def get_id(self, n):
        assert(type(n) == int)
        if n < 0 or n >= len(self.sentences):
            return None
        return self.sentences[n]

    def get_random_id(self):
        return random.choice(self.sentences)

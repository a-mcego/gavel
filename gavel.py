import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()
from collections import Counter
import random
import pathlib

def play_audio(filename, block=True):
    mixer.music.load(filename)
    mixer.music.play()
    if block:
        while mixer.music.get_busy():
            pass

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
        play_audio(self.mp3name)

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

class ActivityTranscription:
    def __init__(self):
        self.description = "Transcribe the audio"

    def do_activity(self, text):
        assert(type(text) == Text)
        current_id = 0
        while True:
            sentence = texts[chosen_text_id].get_id(current_id)
            if sentence is None:
                print("finished the text.")
                break
            translations = sentence.get_translations()
            sentence.play_audio()
            while True:        
                command = input("text/replay/next? ")
                if command == 'text':
                    print(translations[0],end='')
                    sentence.play_audio()
                elif command == 'replay':
                    sentence.play_audio()
                    pass
                elif command == 'next':
                    break
                else:
                    print(f"command '{command}' not understood")
            current_id += 1

class ActivityPlayWhole:
    def __init__(self):
        self.description = "Play whole text"

    def do_activity(self, text):
        assert(type(text) == Text)
        current_id = 0
        while True:
            sentence = texts[chosen_text_id].get_id(current_id)
            if sentence is None:
                print("finished the text.")
                break
            translations = sentence.get_translations()
            print(translations[0],end='')
            sentence.play_audio()
            current_id += 1

def make_choice(arr, text, question):
    arr_with_id = list(zip(range(0,len(arr)),[a.description for a in arr]))
    while True:
        print("-------------------------")
        print(text)
        [print(f"{elem[0]}: {elem[1]}") for elem in arr_with_id]
        try:
            chosen_id = int(input(question))
        except ValueError:
            print("Please give a number.")
            continue
        if chosen_id < 0 or chosen_id >= len(arr):
            print("Please give a valid number.")
            continue
        print("-------------------------")
        return chosen_id



PACK_PATH = "packs"
ACTIVITIES = [ActivityTranscription(),ActivityPlayWhole()]
texts = [Text(os.path.join(PACK_PATH,f)) for f in os.listdir(PACK_PATH) if not os.path.isfile(os.path.join(PACK_PATH, f))]

chosen_text_id = make_choice(texts, "Texts found:", "Choose text number: ")
print(f"Chose {chosen_text_id}: {texts[chosen_text_id].description}")

chosen_activity_id = make_choice(ACTIVITIES, "Activities:", "Choose activity: ")
activity = ACTIVITIES[chosen_activity_id]

print(f"Chose activity '{activity.description}'.")
while True:
    activity.do_activity(texts[chosen_text_id])

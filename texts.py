import random
import os
import pathlib

import audio
import settings
from typing import List

class TagFile: #puts commands in self.commands
    def __init__(self, filename):
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.") #TODO: use an exception here?

        with open(filename, encoding="utf-8") as filehandle:
            lines = filehandle.readlines()

            self.lines = []

            for line in lines:
                line = line.strip() #take off the newline
                if not line: #if line is empty string
                    continue
                splitted = line.split(' ',1)
                command = splitted[0]
                params = None
                if len(splitted) > 1:
                    params = splitted[1]
                
                self.lines.append((command,params))

class Sentence:
    def get_translations(self):
        return [self.target, self.source]

    def play_audio(self):
        audio.play_file(self.audiofile)

class Description:
    def __init__(self, filename):
        description = TagFile(filename)
        for line in description.lines:
            command,params = line
            #todo: better way of doing this bunch of ifs? maybe a list of allowed tags that are set to None by default.
            if command == 'type': #todo: validate type
                self.type = params
            elif command == 'title':
                self.title = params
            elif command == 'target':#todo: validate language
                self.target = params
            elif command == 'source':#todo: validate language
                self.source = params
            elif command == 'description':
                self.description = params
            elif command == 'author':
                self.author = params
            elif command == 'copyright':
                self.copyright = params
            elif command == 'tag':
                self.tag = params
            else:
                print(f"Description command '{command}' not recognised")
            

class Text:
    def __init__(self, path):
        self.path = path
        self.description = Description(os.path.join(self.path,"description.txt"))
        sentencefile = TagFile(os.path.join(self.path,"sentences.txt"))
        self.sentences = [] # type: List[sentence]

        for line in sentencefile.lines:
            command,params = line
            if command == 'sentence':
                self.sentences.append(Sentence())
            elif command == 'audio':
                self.sentences[-1].audiofile = os.path.join(self.path,params)
            elif command == 'target':
                self.sentences[-1].target = params
            elif command == 'source':
                self.sentences[-1].source = params
            else:
                print(f"Sentence command {line} not recognised.")

        print(f"{len(self.sentences)} sentences loaded with text.")

    def get_id(self, n: int):
        if n < 0 or n >= len(self.sentences):
            return None
        return self.sentences[n]

    def get_random_id(self):
        return random.choice(self.sentences)

filenames = [os.path.join(settings.PACK_PATH,f) for f in os.listdir(settings.PACK_PATH)] #type: List[str]
loaded_texts = [Text(filename) for filename in filenames if not os.path.isfile(filename)] # type: List[Text]

import texts

class Activity: #to keep track of all classes
    pass

#every activity must inherit from Activity
class ActivityTranscription(Activity):
    def __init__(self):
        self.description = "Transcribe the audio"

    def do_activity(self, text):
        assert(type(text) == texts.Text)
        current_id = 0
        while True:
            sentence = text.get_id(current_id)
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

class ActivityPlayWhole(Activity):
    def __init__(self):
        self.description = "Play whole text"

    def do_activity(self, text):
        assert(type(text) == texts.Text)
        current_id = 0
        while True:
            sentence = text.get_id(current_id)
            if sentence is None:
                print("finished the text.")
                break
            translations = sentence.get_translations()
            print(translations[0],end='')
            sentence.play_audio()
            current_id += 1

#nice way to get an object of every activity class
all_activities = [class_() for class_ in Activity.__subclasses__()]

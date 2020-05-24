import texts
import views
import tkinter as tk
import tkinter.font as tkf # type: ignore
from functools import partial
import audio

class Activity: #to keep track of all classes
    pass

#every activity must inherit from Activity
class ActivityTranscription(Activity):
    def __init__(self, text):
        self.description = "Transcribe the audio"
        self.current_id = 0
        self.text = text

    def get_current_sentence(self):
        return self.text.get_id(self.current_id)

    def do_activity(self, command):
        assert(type(self.text) == texts.Text)
        sentence = self.get_current_sentence()
        if sentence is None:
            return
        translations = sentence.get_translations()
        if command == 'text':
            print(translations[0],end='')
            sentence.play_audio()
        elif command == 'play':
            sentence.play_audio()
        elif command == 'next':
            self.current_id += 1
            sentence = self.get_current_sentence()
            if sentence is None:
                self.current_id -= 1
                sentence = self.get_current_sentence()
                return
            sentence.play_audio()
        elif command == 'prev':
            if self.current_id > 0:
                self.current_id -= 1
                sentence = self.get_current_sentence()
                if sentence is None:
                    return
                sentence.play_audio()
        else:
            print(f"command '{command}' not understood")

    class View(views.GavelView):
        def update_textbox(self, app, show):
            if show:
                sentence = app.current_act.get_current_sentence()
                self.textbox['text'] = f"Sentence {app.current_act.current_id+1}: {sentence.target}"
            else:
                self.textbox['text'] = f"Sentence {app.current_act.current_id+1}:"

        def prev_button(self, app):
            app.current_act.do_activity('prev')
            self.update_textbox(app, False)

        def next_button(self, app):
            app.current_act.do_activity('next')
            self.update_textbox(app, False)

        def get(self, app, font):
            gui_elements = []
            
            self.label = tk.Label(app, text=app.current_act.description, font=font)
            self.label.pack(side="top")
            gui_elements.append(self.label)

            self.textbox = tk.Label(app, text="", font=font)
            self.textbox.pack(side="top")
            gui_elements.append(self.label)

            self.prev_button = tk.Button(app, text="Prev", command=partial(self.prev_button, app), font=font)
            self.prev_button.pack(side="left")
            gui_elements.append(self.prev_button)

            self.play_button = tk.Button(app, text="(Re)play", command=partial(app.current_act.do_activity, 'play'), font=font)
            self.play_button.pack(side="left")
            gui_elements.append(self.play_button)

            self.show_button = tk.Button(app, text="Show", command=partial(self.update_textbox, app, True), font=font)
            self.show_button.pack(side="left")
            gui_elements.append(self.show_button)

            self.next_button = tk.Button(app, text="Next", command=partial(self.next_button, app), font=font)
            self.next_button.pack(side="left")
            gui_elements.append(self.next_button)

            self.update_textbox(app,False)
            app.current_act.do_activity('play')

            return gui_elements

class ActivityPlayWhole(Activity):
    def __init__(self, text):
        self.description = "Play whole text"
        self.current_id = 0
        self.text = text

    def do_activity(self, command):
        assert(type(self.text) == texts.Text)
        translations = [sentence.get_translations() for sentence in self.text.sentences]
        audio.play_file([s.audiofile for s in self.text.sentences])

    class View(views.GavelView):
        def update_textbox(self, app):
            pass
            #sentence = app.current_act.get_current_sentence()
            #self.textbox['text'] = f"Sentence {app.current_act.current_id+1}: {sentence.target}"

        def get(self, app, font):
            gui_elements = []
            
            self.label = tk.Label(app, text=app.current_act.description, font=font)
            self.label.pack(side="top")
            gui_elements.append(self.label)

            self.textbox = tk.Label(app, text="", font=font)
            self.textbox.pack(side="top")
            gui_elements.append(self.label)

            self.play_button = tk.Button(app, text="(Re)play", command=partial(app.current_act.do_activity, 'play'), font=font)
            self.play_button.pack(side="left")
            gui_elements.append(self.play_button)

            self.update_textbox(app)
            app.current_act.do_activity('play')

            return gui_elements

all_activity_classes = Activity.__subclasses__()

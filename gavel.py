import os
import iso639 # type: ignore
from typing import List, Set, Dict, Tuple, Optional
import tkinter as tk
import tkinter.font as tkf # type: ignore
from functools import partial

#gavel specific stuff
import activities
import texts
import audio
import settings
import views

if not os.path.exists(settings.PACK_PATH):
    os.mkdir(settings.PACK_PATH)
if not os.path.exists(settings.USER_PATH):
    os.mkdir(settings.USER_PATH)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.font = tkf.Font(size=30)
        self.master = master
        self.gui_elements = []

        self.current_view = None
        self.change_view(views.TextView)

    def change_view(self, new_view):
        assert(issubclass(new_view, views.GavelView))

        for elem in self.gui_elements:
            elem.destroy()
        self.current_view = new_view
        self.gui_elements = new_view().get(self, self.font)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.do_quit, font=self.font)
        self.quit.pack(side="bottom")
        self.gui_elements.append(self.quit)
                        

    def choose_text(self, text):
        self.current_text = text
        print(f"playing text: {text.description.title}")
        self.change_view(views.ActivityView)

    def choose_activity(self, act):
        self.current_act = act(self.current_text)
        print(f"doing activity: {act.__name__}")
        self.change_view(self.current_act.View)

    def do_quit(self):
        self.master.destroy()
        audio.stop()

root = tk.Tk()
root.title('Gavel')
app = Application(master=root)
app.mainloop()

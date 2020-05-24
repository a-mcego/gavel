import os
import iso639 # type: ignore
from typing import List, Set, Dict, Tuple, Optional
import tkinter as tk
import tkinter.font as tkf # type: ignore
from functools import partial

#gavel specific stuff
import activities
import texts

class GavelView:
    pass

class TextView(GavelView):
    def get(self, app, font):
        gui_elements = []

        label = tk.Label(app, text="Choose text:", font=font)
        label.pack(side="top")
        gui_elements.append(label)

        for txt in texts.loaded_texts:
            new_button = tk.Button(app, text=txt.description.title, command=partial(app.choose_text,txt), font=font)
            new_button.pack(side="top")
            gui_elements.append(new_button)

        return gui_elements

class ActivityView(GavelView):
    def get(self, app, font):
        gui_elements = []

        label = tk.Label(app, text="Choose activity:", font=font)
        label.pack(side="top")
        gui_elements.append(label)

        for act in activities.all_activity_classes:
            new_button = tk.Button(app, text=act(None).description, command=partial(app.choose_activity,act), font=font)
            new_button.pack(side="top")
            gui_elements.append(new_button)

        return gui_elements

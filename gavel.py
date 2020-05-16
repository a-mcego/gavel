import os

#gavel specific stuff
import activities
import texts
import audio

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
texts = [texts.Text(os.path.join(PACK_PATH,f)) for f in os.listdir(PACK_PATH) if not os.path.isfile(os.path.join(PACK_PATH, f))]

chosen_text_id = make_choice(texts, "Texts found:", "Choose text number: ")
print(f"Chose {chosen_text_id}: {texts[chosen_text_id].description}")

chosen_activity_id = make_choice(activities.all_activities, "Activities:", "Choose activity: ")
activity = activities.all_activities[chosen_activity_id]
print(f"Chose activity '{activity.description}'.")

while True:
    activity.do_activity(texts[chosen_text_id])

from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
used_words = []
current_word = None
flip_timer = None

# choosing random words
def randomize():
    global current_word, flip_timer

    if len(used_words) == len(language_dict):
        used_words.clear()

    available_words = [
        word for word in language_dict if word["German"] not in used_words
    ]
    current_word = choice(available_words)
    used_words.append(current_word["German"])

    canvas.itemconfig(front_image, image=front_card_image)
    canvas.itemconfig(small_text, text="German", fill="black")
    canvas.itemconfig(large_text, text=current_word["German"], fill="black")

    if flip_timer is not None:
        window.after_cancel(flip_timer)
    flip_timer = window.after(3000, count_down)

def is_known():
    language_dict.remove(current_word)
    data = pd.DataFrame(language_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    randomize()
def count_down():
    if current_word is None:
        return
    canvas.itemconfig(front_image, image=back_card_image)
    canvas.itemconfig(small_text, text="English", fill="white")
    canvas.itemconfig(large_text, text=current_word["English"], fill="white")
# Window Setup
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0)
window.title("Flashy")
# Reading data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words.csv")
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = data.to_dict(orient="records")

# Canvas Setup
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
front_image = canvas.create_image(400, 263, image=front_card_image)
small_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
large_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
count_text = canvas.create_text(400, 376, text="", font=("Ariel", 30))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, padx=50, pady=50, borderwidth=0, command=randomize)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, padx=50, pady=50, borderwidth=0, command=is_known)
right_button.grid(column=1, row=1)

randomize()
window.mainloop()


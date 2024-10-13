from tkinter import *
import pandas
import random
random_integer = 0
current_card = {}
data_frame = {}
BACKGROUND_COLOR = "#B1DDC6"

#------------------------------CSV------------------------------#

try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_frame = original_data.to_dict(orient="records")
else:
    data_frame = data_file.to_dict(orient="records")

french_word = data_frame[random_integer]["French"]
english_word = data_frame[random_integer]["English"]

#------------------------------BUTTON------------------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_frame)
    canvas.itemconfig(text, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    data_frame.remove(current_card)
    data = pandas.DataFrame(data_frame)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

#------------------------------FLIPPING CARD------------------------------#

def flip_card():
    canvas.itemconfig(text, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

#------------------------------UI------------------------------#
window = Tk()
window.title("Flashy")
window.geometry("900x750")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_image)  # Top-left corner of the canvas

text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))  # Adjust position as needed
card_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Arial", 60, "bold"))  # Adjust position as needed

unknown_button_image = PhotoImage(file="images/wrong.png")
check_button_image = PhotoImage(file="images/right.png")

unknown_button = Button(image=unknown_button_image, highlightthickness=0, bd=0, command=next_card)
check_button = Button(image=check_button_image, highlightthickness=0, bd=0, command=is_known)

unknown_button.grid(row=1, column=0, padx=50, pady=20)  # Left button
check_button.grid(row=1, column=1, padx=50, pady=20)  # Right button

next_card()
window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Warning", message="You've left something empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {username_entry.get()} \nPassword: {password_entry.get()}")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height= 200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

username = Label(text="Email/Username:")
username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Pass", width=11, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

username_entry.insert(0, "<EMAIL>")
website_entry.focus()

window.mainloop()
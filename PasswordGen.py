import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function to generate a password based on selected strength
def generate_password():
    entry.delete(0, END)  # Clear the current entry field
    length = length_var.get()  # Get the desired length of the password

    # Character sets for different strengths
    low_chars = "abcdefghijklmnopqrstuvwxyz"
    medium_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    high_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"

    password = ""

    # Generate password based on selected strength
    if strength_var.get() == 1:  # Low strength
        for _ in range(length):
            password += random.choice(low_chars)
    elif strength_var.get() == 0:  # Medium strength
        for _ in range(length):
            password += random.choice(medium_chars)
    elif strength_var.get() == 3:  # Strong strength
        for _ in range(length):
            password += random.choice(high_chars)
    else:
        print("Please choose a password strength option")

    return password

# Function to display generated password in the entry field
def generate():
    password = generate_password()
    entry.insert(10, password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    random_password = entry.get()
    pyperclip.copy(random_password)

# Main Function to create GUI window
root = Tk()
strength_var = IntVar()
length_var = IntVar()

# Set the title of the GUI window
root.title("Random Password Generator")

# Label and entry field to display the generated password
password_label = Label(root, text="Password")
password_label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# Label for length of the password
length_label = Label(root, text="Length")
length_label.grid(row=1, column=0)

# Buttons to copy the password to clipboard and generate a new password
copy_button = Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio buttons for selecting the strength of the password
radio_low = Radiobutton(root, text="Low", variable=strength_var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_medium = Radiobutton(root, text="Medium", variable=strength_var, value=0)
radio_medium.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=strength_var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

# Combo box for selecting the length of the password
length_combo = Combobox(root, textvariable=length_var)
length_combo['values'] = tuple(range(8, 33))  # Values from 8 to 32
length_combo.current(0)
length_combo.grid(column=1, row=1)

# Start the GUI loop
root.mainloop()

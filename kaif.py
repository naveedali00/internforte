
from tkinter import *

import random

root = Tk()
root.title("Password Generator")
root.geometry("400x400")

# StringVar to store password string
passstr = StringVar()

# IntVar to store password length
passlen = IntVar()
passlen.set(8)  # Default password length

# Function to generate password
def generate():
    # List of possible characters for the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
             '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', 
             '(', ')']
    
    # Ensure password length is valid
    if passlen.get() > 0:
        password = "".join(random.choice(pass1) for _ in range(passlen.get()))
        passstr.set(password)
    else:
        passstr.set("Invalid length")

# Function to copy the password to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Label and Entry for password length
Label(root, text="Password Generator", font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)

# Button to generate the password
Button(root, text="Generate Password", command=generate).pack(pady=7)

# Entry to show generated password
Entry(root, textvariable=passstr).pack(pady=3)

# Button to copy the generated password to clipboard
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# Start the Tkinter loop
root.mainloop()

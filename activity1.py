# Import necessary libraries
from tkinter import *

# Creat window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# Event handler for keypress
def handle_keypress(event):
    """print the character associeted to the key pressed"""
    print(event.char)

# Bind keypress event to the handle_keypress()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click Me!")
button.pack()

# Bind click event to the handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()
# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup tkinter window
root = Tk()
root.geometry("200x200")

#Function for Displaying warning message
# This call be called once the button is clicked
# messagebox.showwarning("Warning Name", "text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! virus Found.")

# adding Button widget to window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
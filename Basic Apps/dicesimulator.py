# pip install tkinter
import random
from tkinter import *

def dice_roll():
    num_code = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]   # ASCII codes from 1 to 6 in the list
    text_1.config(text = f"{random.choice(num_code)} {random.choice(num_code)}")
    text_1.pack()


root = Tk()   # Tkinter window
root.title("DICE SIMULATOR APP")
root.geometry("600x350")

text_1 = Label(root, text="", font = ("Arial", 250))
button_1 = Button(root, text="Roll the dice", command = dice_roll)
button_1.place(x=250, y=2)

root.mainloop()
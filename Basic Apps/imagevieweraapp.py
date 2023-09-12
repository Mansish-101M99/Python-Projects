# pip install image     pip install tkinter     pip install pillow ; for PIL
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk 
import os

def image_viewer():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(), title="Select Image File", filetype=(("JPG_file","*.jpg"),("PNG_file","*.png"),("JPEG_file","*jpeg")))
    img_1 = Image.open(filename)
    img_1 = ImageTk.PhotoImage(img_1)
    final_label.configure(image = img_1)
    final_label.image = img_1


root = Tk()  # Tkinter window
root.title("IMAGE VIEWER")
root.geometry("600x600")
# root.configure(background="black")

# cover for buttons in app
cover = Frame(root)
cover.pack(side=BOTTOM, padx=15, pady=15)

# Label for appp
final_label = Label(root)
final_label.pack()

# Image view button
btn_1 = Button(cover, text="SELECT-IMAGE", command = image_viewer)
btn_1.pack(side=tk.LEFT)

# App exit button
btn_2 = Button(cover, text="EXIT!", command = lambda:exit())
btn_2.pack(side=tk.LEFT, padx=14)

root.mainloop()

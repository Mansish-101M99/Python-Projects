from tkinter import *
from tkinter import messagebox
import pyspeedtest    # pip install pyspeedtest

def check():
    speed = pyspeedtest.SpeedTest("www.wikipedia.com")
    v1 = (str(speed.download()) + " [Bytes per second]")
    messagebox.showinfo("Your download speed is : ", v1)

root = Tk()
#Basic background for the tab
root.title("Internet Speed Checker")
root.config(bg = "skyblue")
root.geometry("700x350")

label1 = Label(root, text="Internet Speed Checker - ", font=("Arial", 30, "bold"),  bg="green").pack()
button1 = Button(root, text="Click to check", font=("Arial", 22, "bold"), bg="yellow", height=1, width=11, command=check).pack()

root.mainloop()
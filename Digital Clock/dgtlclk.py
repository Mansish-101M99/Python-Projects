
from tkinter import *
from time import strftime

def clk_time():
    st = strftime("%H:%M:%S %p")
    label.config(text=st)   # ---->> To show the above text in the window
    label.after(1000, clk_time)  # 1000 is in milliseconds

root = Tk()   #  --------->> tkinter popup window
root.title("Digital Clock")

label = Label(root, text="Digital Clock", font=("Arial",140,"bold"), fg="lightblue", bg="black")
label.pack(anchor = "center", fill = "both", expand = 1)

clk_time()

root.mainloop()
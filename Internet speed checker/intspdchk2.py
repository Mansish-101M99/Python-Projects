# pip install pillow ; for PIL
# pip install pyspeedtest
import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyspeedtest

# wbst = input("Enter the url to check speed : ")
# spt = pyspeedtest.SpeedTest(wbst)

spt = pyspeedtest.SpeedTest("www.google.com")
def speed_test():
    # spt = pyspeedtest.SpeedTest("www.google.com")
    speed = str(math.floor(spt.download()/1000)) + " [Kb/s]"
    # speed = str(spt.download()/1000) + " [Kb/s]"
    messagebox.showinfo("Your download speed : ",speed) 
    

root = tk.Tk()   #  ------------------------->>  To get a tkinter window
root.geometry("600x450")  # ----------------->>  To have a given (length,bredth)
root.resizable(0,0)   # --------------------->>  To make the window have fixed geometry (x,y)
root.title("Internet Download Speed Checker!!")
root.iconbitmap("wifi_3207.ico")  # --------->>  Icon over the top window.

# Logo
logo = Image.open("Internet speed checker\wifi_wireless_internet_location_pointer_icon_124599.ico")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack(padx=10, pady=8)

# App Widgets
wid_label = tk.Label(root, text="Download Speed Test", font=("Arial",25,"bold"), fg="purple")
wid_label.pack(padx=25, pady=24)

# Buttons
btn1 = tk.Button(root, text="Check", font=("Arial",19,"bold"), background="yellow", command=speed_test)
btn1.pack(padx=20, pady=14)
btn2 = tk.Button(root, text="Stop", command=root.destroy, font=("Arial",19,"bold"), background="yellow")
btn2.pack(padx=15, pady=14)

# New widget label
new_label = tk.Label(root, text="Thanks for Testing", font=("Arial",25,"bold"), fg="green", background="lightblue")
new_label.pack(fill= "both", expand=True)

root.mainloop()
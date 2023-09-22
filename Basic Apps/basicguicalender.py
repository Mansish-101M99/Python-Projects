# pip install tkinter     pip install tkcalendar
from tkinter import *
from tkcalendar import *

def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text = present_date)
    user_date.pack(padx=3, pady=3)


root = Tk()   # Tkinter window
root.geometry("370x350")
root.title("GUI-Calendar")
root.configure(bg="lightgreen")

# Calendar display
display_cal = Calendar(root, setmode = "day", date_pattern = 'dd/mm/yyyy')
display_cal.pack(padx=15, pady=15)

# Date selection button
open_cal = Button(root, text = "SELECT DATE", command = choice_date)
open_cal.pack(padx=15, pady=15)

root.mainloop()
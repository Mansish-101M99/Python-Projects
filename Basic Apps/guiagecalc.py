# pip install tkinter
from tkinter import *
from datetime import date 

root = Tk()  # Tkinter window
root.title("AGE-CALCULATOR")
root.geometry("500x500")

# Day specification
present_date = str( date.today() )
list_today = present_date.split("-")


def age_calc(user_date, user_month, user_year):
    # global today
    global a
    month = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 31, 31]
    
    # Input date
    user_date = int(entry_date.get())
    user_month = int(entry_month.get())
    user_year = int(entry_year.get())
    
    # Present date
    enter_date = int(list_today[2])
    enter_month = int(list_today[1])
    enter_year = int(list_today[0])
    
    if (user_date > enter_date):
        enter_month -= 1
        enter_date = enter_date + month[user_month - 1]
        
    if (user_month > enter_month):
        enter_year -= 1
        enter_month = enter_month + 12
        
    date_result = str(enter_date - user_date)
    month_result = str(enter_month - user_month)
    year_result = str(enter_year - user_year)
    
    # Result shown
    a = Label(root, text="You are\n" + year_result + " YEARS, " + month_result + " MONTHS, and " + date_result + " DAYS " + "OLD.", borderwidth=5)
    a.config(font=("Arial", 17))
    a.grid(row=5, column=0, columnspan=3)
    
    
def clean(entry_date, entry_month, entry_year):
    # Cleaning the input
    entry_date.delete(0, END)
    entry_month.delete(0, END)
    entry_year.delete(0, END)


# Title display
title_label = Label(root, text="AGE-CALCULATOR", borderwidth=6)
title_label.config(font=("Arial", 30))
title_label.grid(row=0, column=0, columnspan=3)

# Date input
date_label = Label(root, text="Date : ", borderwidth=5)
date_label.config(font=("Arial", 15))
date_label.grid(row=1, column=0, columnspan=1)

# Month input
month_label = Label(root, text="Month : ", borderwidth=5)
month_label.config(font=("Arial", 15))
month_label.grid(row=2, column=0, columnspan=1)

# Year input
year_label = Label(root, text="Year : ", borderwidth=6)
year_label.config(font=("Arial", 15))
year_label.grid(row=3, column=0, columnspan=1)

entry_date = Entry(root, width=20, borderwidth=6)
entry_month = Entry(root, width=20, borderwidth=6)
entry_year = Entry(root, width=20, borderwidth=6)

entry_date.grid(row=1, column=2)
entry_month.grid(row=2, column=2)
entry_year.grid(row=3, column=2)

user_date = entry_date.get()
user_month = entry_month.get()
user_year = entry_year.get()

final = Button(root, text="Give Age !!", width=10, anchor=CENTER, command = lambda:age_calc(user_date, user_month, user_year), bg="yellow", borderwidth=4)
final.grid(row=4, column=0)

clear_btn = Button(root, text="CLEAR", width=10, command = lambda:clean(entry_date, entry_month, entry_year), bg="green", borderwidth=4)
clear_btn.grid(row=4, column=2)

root.mainloop()
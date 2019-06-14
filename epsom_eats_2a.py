# display window
# display title
# display pre order and start order buttons
# display time
# enable / disable buttons based on time 

from tkinter import *
from tkinter import ttk
import datetime
import time

def start_screen():
    # keeps time ticking
    global time1
    time1 = ''
    global clock
    clock = Label(root)
    clock.pack(anchor = "nw", padx = 10, pady = 10)
    tick()
    
    ttk.Label(root, text = "Epsom Eats", font=('verdana', 50)).pack(expand=YES)
    global preorder_button
    preorder_button = ttk.Button(root, text = "Pre Order", state = check_preorder_time())
    global start_button
    start_button = ttk.Button(root, text = "Start Order", state = check_startorder_time())

    preorder_button.pack(side = BOTTOM, pady = 50)
    start_button.pack(side = BOTTOM, pady = 10)

    update_buttons()

def update_buttons():
    preorder_button.config(state = check_preorder_time())
    preorder_button.update()

    start_button.config(state = check_startorder_time())
    start_button.update()

    root.after(1000, update_buttons)

# clock code below modified from https://stackoverflow.com/questions/15689667/digital-clock-in-status-bar-in-python-3-and-tkinter
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%I:%M %p').lstrip("0").replace(" 0", " ")
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(1000, tick)

def week_day():
    return datetime.datetime.today().weekday()
    
def check_preorder_time():
    
    deadlines = [1225, 1225, 1235, 1225, 1250]
    deadline = deadlines[week_day()]
    if int(time.strftime('%H%M')) >= deadline:
        return "disabled"
    else:
        return "enabled"

def check_startorder_time():

    deadlines = [1255, 1255, 1305, 1255, 1245]
    deadline = deadlines[week_day()]
    if int(time.strftime('%H%M')) >= deadline:
        return "disabled"
    else:
        return "enabled"

if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0) # disable resizing

    ttk.Style().configure("TButton", justify = "center")
    
    # places start screen contents
    start_screen = start_screen()
    
    root.mainloop()

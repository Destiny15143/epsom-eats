# pre order ask for input
# link to component 1 (start screen)

from tkinter import *
from tkinter import ttk
from functools import partial
import csv
import datetime
import time

class Food:
    def __init__(self, row, header):
        #initiates each row as an instance and headings as their attributes -(from https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class)
        self.__dict__ = dict(zip(header, row)) 

    # methods to access attributes using index 
    def find_food_name(i):
        return(foods[i].food_name)
    def find_category(i):
        return(foods[i].category)
    def find_price(i):
        return(foods[i].price)
    def find_description(i):
        return(foods[i].category)

    # find index of food based on food name 
    def find_index(i):
        count = 0
        for food in foods:
            if food.food_name == i:
                break
            else:
                count += 1
        return count

    # adds each food_name into their respective list based on category
    def categorise():
        hot_food_names = []
        chilled_food_names = []
        treats_food_names = []
        for i in range(len(foods)):
            if Food.find_category(i) == "Chilled":
                chilled_food_names.append(Food.find_food_name(i))
            elif Food.find_category(i) == "Hot":
                hot_food_names.append(Food.find_food_name(i))
            else:
                treats_food_names.append(Food.find_food_name(i))
        return chilled_food_names, hot_food_names, treats_food_names

class pageGrid:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = "Title goes here").grid(row = 0, column = 0)

        # places category frames in window
        self.chilled_content = ttk.Frame(master)
        self.chilled_content.pack(side = LEFT, anchor = "n", expand = YES)
        self.hot_content = ttk.Frame(master)
        self.hot_content.pack(side = LEFT, anchor = "n", expand = YES)
        self.treats_content = ttk.Frame(master)
        self.treats_content.pack(side = LEFT, anchor = "n", expand = YES)

        # places button groups in their respective categories
        buttonGrid(self.chilled_content, chilled_button_string)
        buttonGrid(self.hot_content, hot_button_string)
        buttonGrid(self.treats_content, treats_button_string)

class preorderDialogue:
    def __init__(self, parent):
        
        top = self.top = Toplevel(parent)
        top.attributes("-topmost", True) #stays on top
        coord = center_window(300, 200)
        top.geometry("300x200+{}+{}".format(str(coord[0]), str(coord[1])))        
        
        self.prompt = Label(top, text = "Enter your student ID below").grid(row = 0, column = 0, columnspan = 4, pady = 30, padx = 37.5)
        self.entry_field = Entry(top)        
        self.entry_field.grid(row = 1, column = 0, columnspan = 4, padx = 37.5)
        self.place_holder = Label(self.top).grid(row = 2, column = 0, columnspan = 4, pady = 5, padx = 37.5) # place holder for error message text 
        self.top.resizable(0,0)

        ok = ttk.Button(top, text = "Ok", command = self.ok)
        ok.grid(row = 3, column = 0, columnspan = 2, pady = 20, padx = 37.5)
        cancel = ttk.Button(top, text = "Cancel", command = self.cancel)
        cancel.grid(row = 3, column = 2, columnspan = 2, pady = 20, padx = 37.5)

    def ok(self):
        valid = False


        # checks for valid input
        try: 
            preorder_id = int(self.entry_field.get())

            if 15000 <= preorder_id <= 19999:
                start_menu()
                self.top.destroy()
                valid = True
            else:
                self.entry_field.delete(0, 'end') # clear input field
                self.error_msg = Label(self.top, text = "Please enter a valid student ID").grid(row = 2, column = 0, columnspan = 4, pady = 5, padx = 37.5)
                root.after(1000, update_buttons)

        except ValueError:
            self.entry_field.delete(0, 'end')
            self.error_msg = Label(self.top, text = "Please enter a valid student ID").grid(row = 2, column = 0, columnspan = 4, pady = 5, padx = 37.5)
            root.after(1000, update_buttons)

    def cancel(self):
        self.top.destroy()


# places a category of buttons
class buttonGrid():

    def __init__(self, master, food_names): 
        
        num_rows = self.calculate_rows(food_names)
        NUM_COLS = 2
        buttons = []
        count = 0
        for c in range(NUM_COLS):
            for r in range(num_rows):
                if count < len(food_names):
                    food_name = food_names[count]
                    # prepares food name and price in a tidy format 
                    output = "{} \n${:.2f}".format(food_name[0], float(food_name[1]))
                    # partial code module from https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter/22290388
                    buttons.append(ttk.Button(master, text = output, width = 20, command = partial(quantity_selection, food_name[0])))
                    buttons[count].grid(row = r, column = c)
                    count += 1
                
    # number of rows required to format all food names into two columns                 
    def calculate_rows(self, food_names):
            rows = len(food_names) / 2
            if len(food_names) % 2 != 0:
                rows += 0.5
            return int(rows)

    # to be used on button output
    def food_name_price(food_names):
        return_string = []
        for i in food_names:
            sub_list = []
            # adds food name and its corresponding price as a sublist into the returned string
            # adds food name
            sub_list.append(i)
            # finds corresponding index then price
            sub_list.append(Food.find_price(Food.find_index(i))) 
            return_string.append(sub_list)
        return return_string

# will be combined with quantity selection pop up component later 
def quantity_selection(food_name): 
    print(food_name)

def start_screen():
    # keeps time ticking
    global time1
    time1 = ''
    global clock
    clock = Label(root)
    clock.pack(anchor = "nw", padx = 10, pady = 10)
    tick()
    global title
    title = ttk.Label(root, text = "Epsom Eats", font=('verdana', 50))
    global preorder_button
    preorder_button = ttk.Button(root, text = "Pre Order", state = check_preorder_time(), command = partial(preorder))
    global start_button
    start_button = ttk.Button(root, text = "Start Order", state = check_startorder_time(), command = partial(start_menu))
    preorder_button.pack(side = BOTTOM, pady = 50)
    start_button.pack(side = BOTTOM, pady = 10)
    title.pack(expand=YES)
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
    
def check_preorder_time():
    deadlines = [1225, 1225, 1235, 1225, 1250]
    deadline = deadlines[datetime.datetime.today().weekday()] # finds day of the week as index
    if int(time.strftime('%H%M')) >= deadline:
        return "disabled"
    else:
        return "enabled"

def check_startorder_time():
    deadlines = [1255, 1255, 1305, 1255, 1245]
    deadline = deadlines[datetime.datetime.today().weekday()] # finds day of the week as index
    if int(time.strftime('%H%M')) >= deadline:
        return "disabled"
    else:
        return "enabled"

def preorder():
    d = preorderDialogue(root)
    root.wait_window(d.top)
    
def start_menu():
    page_grid = pageGrid(root)
    preorder_button.forget()
    start_button.forget()
    title.forget()

def center_window(window_width, window_height):

    coord = []
    pos_right = int(root.winfo_screenwidth()/2 - window_width/2)
    pos_down = int(root.winfo_screenheight()/2 - window_height/2)
    coord.append(pos_right)
    coord.append(pos_down)
    return coord

if __name__ == "__main__":

    root = Tk()
    root.overrideredirect(1) # clears min/max buttons, close buttons
    coord = center_window(1000, 600)
    root.geometry("1000x600+{}+{}".format(str(coord[0]), str(coord[1])))
    ttk.Style().configure("TButton", justify = "center")

    #opens menu file 
    data = list(csv.reader(open('menu.csv')))
    #passes in heading and rest of rows and collects instances into list
    foods = [Food(i, data[0]) for i in data[1:]]

    # extracts food_names as lists in each category
    chilled_button_string = buttonGrid.food_name_price(Food.categorise()[0])
    hot_button_string = buttonGrid.food_name_price(Food.categorise()[1])
    treats_button_string = buttonGrid.food_name_price(Food.categorise()[2])

    # places start screen contents
    start_screen = start_screen()
    root.mainloop()
    

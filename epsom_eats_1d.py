# display prices with food name 
# button commands should return food_name 

import csv
from tkinter import *
from tkinter import ttk
from functools import partial

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
        button_grid(self.chilled_content, chilled_button_string)
        button_grid(self.hot_content, hot_button_string)
        button_grid(self.treats_content, treats_button_string)

# places a category of buttons
def button_grid(master, food_names):
        
    num_rows = calculate_rows(food_names)
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
def calculate_rows(food_names):
        rows = len(food_names) / 2
        if len(food_names) % 2 != 0:
            rows += 0.5
        return int(rows)
    
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

if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0) # disable resizing

    ttk.Style().configure("TButton", justify = "center")
    
    #opens menu file 
    data = list(csv.reader(open('menu.csv')))
    #passes in heading and rest of rows and collects instances into list
    foods = [Food(i, data[0]) for i in data[1:]]

    # extracts food_names as lists in each category
    chilled_button_string = food_name_price(categorise()[0])
    hot_button_string = food_name_price(categorise()[1])
    treats_button_string = food_name_price(categorise()[2])

    #places page contents
    page_grid = pageGrid(root) 
    
    root.mainloop()    

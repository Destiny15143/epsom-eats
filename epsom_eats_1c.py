# organise content into frames - heading and category
# place groups of buttons into category frames

import csv
from tkinter import *
from tkinter import ttk

class Food:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row)) #initiates each row as an instance and headings as their attributes
    def find_food_name(i):
        return(foods[i].food_name) #access food name from instance
    def find_category(i):
        return(foods[i].category)

def button_grid(master, food_names):

    def calculate_rows():
        rows = len(food_names) / 2
        if len(food_names) % 2 != 0:
            rows += 0.5
        return int(rows)

    
    NUM_ROWS = calculate_rows()
    NUM_COLS = 2
    buttons = []

    count = 0
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            if count < len(food_names):
                food_name = food_names[count]
                buttons.append(ttk.Button(master, text = food_name, width = 13))
                buttons[count].grid(row = r, column = c)
                count += 1

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
        button_grid(self.chilled_content, chilled_food_names)
        button_grid(self.hot_content, hot_food_names)
        button_grid(self.treats_content, treats_food_names)

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


if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0) # disable resizing

    #opens menu file 
    data = list(csv.reader(open('menu.csv')))
    #passes in heading and rest of rows and collects instances into list
    foods = [Food(i, data[0]) for i in data[1:]] 

    # extracts food_names as lists in each category
    chilled_food_names = categorise()[0]
    hot_food_names = categorise()[1]
    treats_food_names = categorise()[2]
    #button_category = buttonGrid(root, treats_food_names)

    page_grid = pageGrid(root)
    

    root.mainloop()    

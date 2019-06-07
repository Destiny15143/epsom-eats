# epsom_eats_1b

# 1a and...
# categorises foods (chilld, hot, treats)

import csv

class Food:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row)) #initiates each row as an instance and headings as their attributes (from https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class)
    def find_food_name(i):
        return(foods[i].food_name) #access food name from instance (testing purposes)
    def find_category(i):
        return(foods[i].category)

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

    #opens menu file 
    data = list(csv.reader(open('menu.csv')))
    #passes in heading and rest of rows and collects instances into list
    foods = [Food(i, data[0]) for i in data[1:]] 

    # extracts food_names as lists in each category
    chilled_food_names = categorise()[0]
    hot_food_names = categorise()[1]
    treats_food_names = categorise()[2]

    # print categories (testing)
    print(chilled_food_names)
    print()
    print(treats_food_names)
    print()
    print(hot_food_names)

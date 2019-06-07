# puts csv file into class
# assigns headings as each food's attributes
# their food name is assumed to be unique so will serve as their ID 

import csv

class Food:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row)) #initiates each row as an instance and headings as their attributes (from https://stackoverflow.com/questions/47445586/how-to-read-the-contents-of-a-csv-file-into-a-class-with-each-csv-row-as-a-class)
    def find_food_name(i):
        return(foods[i].food_name) #access food name from instance (testing purposes)


if __name__ == "__main__":

    #opens menu file 
    data = list(csv.reader(open('menu.csv')))
    #passes in heading and rest of rows and collects instances into list
    foods = [Food(i, data[0]) for i in data[1:]] 
    print(Food.find_food_name(5)) # outputs 6th food item (Croissants)

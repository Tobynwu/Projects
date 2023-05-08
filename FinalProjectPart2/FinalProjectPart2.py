"""
Tobenna Nwufo
2054054
CIS 2348
"""

import csv
from datetime import datetime

# dictionary creation function


def read_csv(file_name):
    data = {}  # creates the dictionary
    with open(file_name, 'r') as f:  # opens and reads data from specified csv file
        reader = csv.reader(f)
        for row in reader:
            data[row[0]] = [value.strip() for value in row[1:]]  # removes whitespace from each value and gets the values for each ID
    return data  # returns the ID for each value

# key for sorting combined inventory


def sort_inventory(item):
    item_id, item_data = item  # unpacking the ID number into one variable and the data from that ID into the other variable
    return (item_data[0], item_id)  # returning the manufacturing name and item_id

# function to find closest item in price to given item


def find_closest_item(inventory, item_type, price, manu_name):
    closest_item = None # the closest item starts off as none
    closest_price_diff = float('inf') # sets the current distance to positive infinity
    for item_id, item_data in inventory.items(): # iterates through the inventory
        if item_data[1] == item_type and item_data[4] != 'damaged' and datetime.strptime(item_data[3], '%m/%d/%Y') > datetime.now() and item_data[0] != manu_name:
            item_price = float(item_data[2]) # get the items price
            price_diff = abs(item_price - price) # get the price difference by subtracting from the items price
            if price_diff < closest_price_diff:
                closest_item = item_data # gets the closest item
                closest_price_diff = price_diff # gets the price difference from the closest item
    return closest_item

# read in the csv files and combine into one inventory


manu_dict = read_csv('ManufacturerList.csv')
price_dict = read_csv('PriceList.csv')
service_dict = read_csv('ServiceDatesList.csv')
inventory = {}
for item_id in manu_dict:
    if item_id in price_dict and item_id in service_dict:
        manu, item_type, damaged = manu_dict[item_id]
        price = price_dict[item_id][0]
        service_date = service_dict[item_id][0]
        inventory[item_id] = [manu, item_type, price, service_date, damaged]
manu_set = (set([data[0] for data in inventory.values()])) # makes set for manufacturing names
type_set = (set([data[1] for data in inventory.values()]))  # makes set for item type
# full_set = manu_set | type_set
# start the query loop
while True:
    # get input from user
    user_input = input("Type a query or 'q' to quit: ")
    manu_input = "" # creating blank variable
    item_type_input = "" # creating blank variable
    if user_input == 'q':
        break
    user_input = user_input.split(' ') # makes the user input into list of words
    for curr in user_input: # iterate through the list of words made from the input
        if curr in manu_set: # check if the word from input is in the manufacturing name set
            manu_input = curr # make manu_input take on the value of the word in the set
    for curr_i in user_input:
        if curr_i in type_set:
            item_type_input = curr_i
    # search inventory for items matching user input
    matching_items = [] # create empty list to hold matching input
    for item_id, item_data in inventory.items():
        if item_data[0] == manu_input and item_data[1] == item_type_input and item_data[4] != 'damaged' and datetime.strptime(item_data[3], '%m/%d/%Y') > datetime.now():
            matching_items.append((item_id, item_data))
    # print results
    if len(matching_items) == 0: # if the list is empty
        print("No such item in inventory")
    elif len(matching_items) == 1: # if the list has been populated
        item_id, item_data = matching_items[0] # unpack the list into the 2 different variables
        print(f"Your item is: {item_id} {item_data[0]} {item_data[1]} {item_data[2]}")
        closest_item = find_closest_item(inventory, item_data[1], float(item_data[2]), item_data[0])
        if closest_item is not None: # if there is a valid closest item
            print(f"You may also consider: {closest_item[0]} {closest_item[1]} {closest_item[2]} {closest_item[3]}")
    elif len(matching_items) > 1: # if there is more than 1 iteration of one word in the list
        print("No such item in inventory")


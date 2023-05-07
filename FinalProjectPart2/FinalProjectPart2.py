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
    closest_price_diff = float('inf')
    for item_id, item_data in inventory.items():
        if item_data[1] == item_type and item_data[4] != 'damaged' and datetime.strptime(item_data[3], '%m/%d/%Y') > datetime.now() and item_data[0] != manu_name:
            item_price = float(item_data[2])
            price_diff = abs(item_price - price)
            if price_diff < closest_price_diff:
                closest_item = item_data
                closest_price_diff = price_diff
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
manu_set = (set([data[0] for data in inventory.values()]))
type_set = (set([data[1] for data in inventory.values()]))
full_set = manu_set | type_set
# start the query loop
while True:
    # get input from user
    user_input = input("Type a query or 'q' to quit: ")
    manu_input = ""
    item_type_input = ""
    if user_input == 'q':
        break
    user_input = user_input.split(' ')
    for curr in user_input:
        if curr in manu_set:
            manu_input = curr
    for curr_i in user_input:
        if curr_i in type_set:
            item_type_input = curr_i
    # search inventory for items matching user input
    matching_items = []
    for item_id, item_data in inventory.items():
        if item_data[0] == manu_input and item_data[1] == item_type_input and item_data[4] != 'damaged' and datetime.strptime(item_data[3], '%m/%d/%Y') > datetime.now():
            matching_items.append((item_id, item_data))
    # print results
    if len(matching_items) == 0:
        print("No such item in inventory")
    elif len(matching_items) == 1:
        item_id, item_data = matching_items[0]
        print(f"Your item is: {item_id} {item_data[0]} {item_data[1]} {item_data[2]}")
        closest_item = find_closest_item(inventory, item_data[1], float(item_data[2]), item_data[0])
        if closest_item is not None:
            print(f"You may also consider: {closest_item[0]} {closest_item[1]} {closest_item[2]} {closest_item[3]}")
    elif len(matching_items) > 1:
        print("No such item in inventory")


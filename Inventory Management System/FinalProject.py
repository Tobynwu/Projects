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
            data[row[0]] = row[1:]  # the id becomes the key for each entry in the dictionary
    return data  # the data connected to the Id is then returned

# key for sorting combined inventory
def sort_inventory(item):
    item_id, item_data = item  # unpacking the ID number into one variable and the data from that ID into the other variable
    return (item_data[0], item_id)  # returning the manufacturing name and item_id


manu_dict = read_csv('ManufacturerList.csv')  # getting the manufacturing dictionary
price_dict = read_csv('PriceList.csv')  # getting the price dictionary
service_dict = read_csv('ServiceDatesList.csv')  # getting the service date dictionary

# making the 3 dictionaries created one whole

inventory = {}  # making the dictionary that will hold all the other 3 dictionaries combined
for item_id in manu_dict:  # going through all the ids in the manufacturing dictionary
    if item_id in price_dict and item_id in service_dict:  # checking if the ID is in all the dictionaries
        manu, item_type, damaged = manu_dict[item_id]  # unpacking the data from each ID in the manufacturing dictionary
        price = price_dict[item_id][0]  # unpacking the price from each ID
        service_date = service_dict[item_id][0]  # unpacking the date from each ID
        inventory[item_id] = [manu, item_type, price, service_date, damaged]  # repacking all the data into one dictionary

sorted_inventory = sorted(inventory.items(), key=sort_inventory) # .items() turns the inventory into a collection of tuples which are then sorted by the key made in sort_inventory)
# create the four output files

# FullInventory.csv
with open('FullInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for item_id, item_data in sorted_inventory:  # goes through each tuple in the list that is sorted_inventory
        writer.writerow([item_id] + item_data) # writes the ID and the following information from it


# Item type Inventory list
for item_type in set([data[1] for data in inventory.values()]):  # creates a set to hold the item types then iterates over the s
    with open(f'{item_type}Inventory.csv', 'w', newline='') as f:  # uses the item type to create the name for written file
        writer = csv.writer(f)
        for item_id, item_data in sorted_inventory:  # goes through each tuple in the list that is sorted_inventory
            if item_data[1] == item_type:  # if the item type in th tuple equals the item type in the set
                writer.writerow([item_id] + item_data)  # that item ID is selected along with the rest of the data for that ID

today = datetime.now() # gets the current date
# PastServiceDateInventory.csv
with open('PastServiceDateInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for item_id, item_data in sorted_inventory:  # goes through each tuple in the list that is sorted_inventory
        if datetime.strptime(item_data[3], "%m/%d/%Y") < today and item_data[3] != '':  # if the date in the tuple is less than todays date
            writer.writerow([item_id] + item_data) # write the ID plus the data

# DamagedInventory.csv
with open('DamagedInventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for item_id, item_data in sorted_inventory: # goes through each tuple in the list that is sorted_inventory
        if item_data[4] == 'damaged':  # if 'damaged' is in the tuple
            writer.writerow([item_id] + item_data[0:4])  # write the ID plus th date, name, and item_type
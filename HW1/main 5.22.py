# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348
"""
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

first_service = input("\nSelect first service:\n")
second_service = input("Select second service:\n")
print("\nDavy's auto shop invoice\n")
total = 0
# first service
if first_service == "Oil change":
    print("Service 1: Oil change, $35")
    total += 35
elif first_service == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    total += 19
elif first_service == "Car wash":
    print("Service 1: Car wash, $7")
    total += 7
elif first_service == "Car wax":
    print("Service 1: Car wax, $12")
    total += 12
elif first_service == "-":
    print("Service 1: No service")
#second service   
if second_service == "Oil change":
    print("Service 2: Oil change, $35")
    total += 35
elif second_service == "Tire rotation":
    print("Service 2: Tire rotation, $19")
    total += 19
elif second_service == "Car wash":
    print("Service 2: Car wash, $7")
    total += 7
elif second_service == "Car wax":
    print("Service 2: Car wax, $12")
    total += 12
elif second_service == "-":
    print("Service 2: No service")
    
print("\nTotal: $"+str(total))




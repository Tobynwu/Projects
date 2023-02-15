# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348
"""
print("==================================")
print("Birthday Calander")
current_day = int(input("Please enter current day:\n"))
current_month = int(input("Please enter current month in number form:\n"))
current_year = int(input("Please enter current year: \n"))
print("----------------------------------")
b_day = int(input("Please enter the day of your birthday:\n"))
b_month = int(input("Please enter the month of your birthday in number form:\n"))
b_year = int(input("Please enter the month of your birthday:\n"))
age = current_year - b_year
if(b_month > current_month):
    age -= 1
elif(current_month == b_month):
    if(b_day < current_day):
        age -= 1
print("___________________________________")
print("You are",age,"years old!")
if (current_day==b_day) and (current_month == b_month):
    print("Happy Birthday!!")
print("==================================")

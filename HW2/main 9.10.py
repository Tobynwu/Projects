# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:56:10 2023

@author: a1233
""" 
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 
             'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 
             'November': 11, 'December': 12}
             
try:
    outFile = open('parsedDates.txt', 'w')
    with open('inputDates.txt', 'r') as file:
        for date in file:
            date = date.strip()
            if date == '-1':
                break 
            monthIndex = date.find(" ")
            dayIndex = date[monthIndex+1:].find(", ")
            if monthIndex != -1 and dayIndex != -1:
                month = date[:monthIndex] 
                day = date[monthIndex+1:][:dayIndex]
                year = date[monthIndex+1:][dayIndex+2:]
                monthNum = month_dict[month] 
                outFile.write(str(monthNum) + '/' + day + '/' + year + '\n')
except FileNotFoundError:
    print('Error: Input file not found')
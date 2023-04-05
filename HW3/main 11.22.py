# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""

data = input().split()

for word in data:
    count = 0
    for item in data:
        if word == item:
            count += 1
    print(word, count)
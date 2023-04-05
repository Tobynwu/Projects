# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""
nums = input()
lst = nums.split()

new_list = []

for i in lst:
    if int(i) >= 0:
        new_list.append(int(i))

new_list.sort()

for x in new_list:
    print(x, end=' ')

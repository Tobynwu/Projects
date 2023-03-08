# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""

inputs=str(input())
noSpace=inputs.replace(' ', '')
reverse_input=noSpace
reverse_input=reverse_input[::-1]
if reverse_input==noSpace:
    print (inputs, 'is a palindrome')
else:
    print(inputs, 'is not a palindrome')
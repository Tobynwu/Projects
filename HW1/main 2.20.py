# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""
#Part 1
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields {:.2f}".format(servings)+ " servings")
print("{:.2f}".format(lemon)+" cup(s) lemon juice")
print("{:.2f}".format(water)+" cup(s) water")
print("{:.2f}".format(nectar)+" cup(s) agave nectar")

#Part2
new_servings = float(input("\nHow many servings would you like to make?\n"))
print()
ratio = new_servings/servings
servings = new_servings
lemon =lemon*ratio
water = water*ratio
nectar = nectar*ratio

print("Lemonade ingredients - yields {:.2f}".format(servings)+ " servings")
print("{:.2f}".format(lemon)+" cup(s) lemon juice")
print("{:.2f}".format(water)+" cup(s) water")
print("{:.2f}".format(nectar)+" cup(s) agave nectar")

#Part 3
gallons  = 16
lemon = lemon/gallons
water = water/gallons
nectar= nectar/gallons
print()
print("Lemonade ingredients - yields {:.2f}".format(servings)+ " servings")
print("{:.2f}".format(lemon)+" gallon(s) lemon juice")
print("{:.2f}".format(water)+" gallon(s) water")
print("{:.2f}".format(nectar)+" gallon(s) agave nectar")

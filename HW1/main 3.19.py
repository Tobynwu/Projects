# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""
import math

paint_color={'red':35, 'blue':75, 'green':23}

Height=int(input("Enter wall height (feet):\n"))
Width=int(input('Enter wall width (feet):\n'))
Area= Height * Width
print("Wall area:",Area,"square feet")

paint_needed = "{:.2f}".format(Area/350,6)
print("Paint needed:" ,paint_needed, "gallons")
paint_final=round(Area/350,6)
cans=math.ceil(paint_final)

print("Cans needed:",cans,"can(s)\n")

color_chose=input("Choose a color to paint the wall:\n")
print("Cost of purchasing",color_chose,"paint: $"+str(paint_color[color_chose]))
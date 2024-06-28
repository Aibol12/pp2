#Write a Python program to calculate the area of a trapezoid.

import math 

def areaOfTrap( h, v1, v2):
    return h*((v1+v2)*0.5)

print( areaOfTrap( 5, 5, 6))
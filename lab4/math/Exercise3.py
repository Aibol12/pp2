#Write a Python program to calculate the area of regular polygon.

import math 

def areaOfRegPol( v1, v2):
    apothem = v2 / 2*math.tan(math.pi/v1) 
    return v1 * v2 * 0.5 * apothem


print( areaOfRegPol( 4, 25 ))
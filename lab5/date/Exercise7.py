#Write a python program to convert snake case string to camel case string.
import re
def snake_to_camel(string):
    return "".join(i.capitalize() for i in string.split('_') )

string = input()
print(snake_to_camel(string))
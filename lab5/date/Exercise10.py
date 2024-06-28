#Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(string):
    return (re.sub(r'(.)([A-Z])', r'\1_\2', string)).lower()

string = input()
print(camel_to_snake(string))
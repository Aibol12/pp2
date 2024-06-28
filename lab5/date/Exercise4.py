#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
def find(text):
    pattern = '[A-Z]+[a-z]+'
    return True if re.search(pattern, text) else False

text = input()
print(find(text))
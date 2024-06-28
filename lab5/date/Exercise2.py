#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
def match(text):
    pattern = 'ab{2,3}'
    return True if re.search(pattern, text) else False

text = input()
print(match(text))
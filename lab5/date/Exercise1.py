#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def f(text):
    pattern = '^a(b*)$'
    return True if re.search(pattern, text) else False

text = input()
print(f(text))
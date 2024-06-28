#Write a Python program to replace all occurrences of space, comma, or dot with a colon.Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def r(text):
    return re.sub('[ ,.]', ':', text)

text = input()
print(r(text))
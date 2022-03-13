import re
a = input()
x = re.findall("[A-Z][^A-Z]*", a)
print(x)
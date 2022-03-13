import re
a = input()
z= re.findall("[A-Z][^A-Z]*", a)
for i in z:
 print(i, end = ' ')
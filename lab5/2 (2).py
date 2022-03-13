import re
a = input()
x = re.search('a(b{2,3})',a)
if x:
    print("Yes")
else :
    print("No")
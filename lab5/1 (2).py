import re
a = input()
y = re.search('^a(b*)',a)
if y:
    print("Yes")
else :
    print("No")
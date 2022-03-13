import re
a = input()
y= re.search('^a+[\w]+b+$',a)
if y:
    print("Yes")
else :
    print("No")


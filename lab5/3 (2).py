import re
a = input()
x = re.search('^[a-z]+_[a-z]+$',a)
if x:
    print("Yes")
else :
    print("No")
print(x)

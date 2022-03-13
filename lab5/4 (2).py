import re
a= input()
y = re.search('[A-Z]_[a-z]+$',a)
if y:
    print("Yes")
else :
    print("No")
print(y)

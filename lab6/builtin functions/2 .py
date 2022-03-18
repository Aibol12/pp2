n = input()
a = 0
b = 0
for i in n:
    if(i.isalpha()):
        if(i.isupper()):
            a += 1
        else:
            b += 1
print(a)
print(b)

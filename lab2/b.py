n=int(input())
txt=str(input())
x=txt.split()
for i in range (n):
    x[i]=int(x[i])
x.sort()
print(x[len(x)-1]*x[len(x)-2])


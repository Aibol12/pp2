from math import sqrt

x=input().split()
x[0]=int(x[0])
x[1]=int(x[1])
n=int(input())
a=[]
def alp(step):
    return step[2]
for i in range(n):
    a.append([])
    a[i]=input().split()
    a[i][0]=int(a[i][0])
    a[i][1]=int(a[i][1])
    a[i].append(float(sqrt((abs(a[i][0]-x[0]))**2+(abs(a[i][1]-x[1]))**2)))
a=sorted(a, key= alp)
for i in range(n):
    print(f'{a[i][0]}',f'{a[i][1]}')
txt=input().split()
if len(txt)==2:
    n=int(txt[0])
    x=int(txt[1])
else:
    n=int(txt[0])
    x=int(input())
a=[]
for i in range(x, x+2*n, 2):
    a.append(i)
answer=a[0]
for i in range(n-1):
    answer=answer^a[i+1]
print(answer)
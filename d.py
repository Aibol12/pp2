a=int(input())
b=str(input())
d=float(0.0)
e=float(0.0)
if b=='k' :
   c=int(input())
   d= a / 1024
   e= round(d, c)
   print(e)
if b=='b':
    d= a*1024
    print(d)
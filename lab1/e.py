from math import sqrt
txt=str(input())
dist=int(txt.split()[0])
n=int(txt.split()[1])
def isprime(n):
   for i in range(2,int(sqrt(n))+1):
       if n%i==0:
           return False
   return  True
if isprime(dist) and dist<500 and n%2==0:
   print("Good job!")
else:
   print("Try next time!"))

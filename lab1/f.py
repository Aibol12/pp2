n=int(input())
b=[]
for i in range(n):
   b.append(int(input()))
for i in range(len(b)):
   if b[i]<=10 :
       print('Go to work!')
   if 10>b[i] and b[i]<=25 :
       print('You are weak')
   if b[i]>25 and b[i]<=45 :
       print('Okay, fine')
   if 45<b[i] :
       print('Burn! Burn! Burn Young!')

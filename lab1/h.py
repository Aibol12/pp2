s= str(input())
t=str(input())
ans=""
for i in range (len(s)):
  if t in s[i]:
    ans+=str(i)+ " "
Aibol=ans.split()
if(len(Aibol)>2):
   print (Aibol[0]+ " "+ Aibol[len(Aibol)-1])
if(len(Aibol))==1:
   print(Aibol[0])
if(len(Aibol))==2:
   print(Aibol[0]+" "+Aibol[1])     




  

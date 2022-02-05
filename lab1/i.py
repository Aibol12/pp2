n=int(input())
a=[]
for i in range(n):
   a.append(str(input()))
for i in a:
   if i[len(i)-10:len(i)]=="@gmail.com":
       i=i[0:len(i)-10]
       print(i)

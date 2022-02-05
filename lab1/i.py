a= int(input())
ans = ""
for i in range(a):
    b = (input())
    if "@" in b:
      tv = b.split("@")
      if tv[1] == "gmail.com":
         ans += tv[0] + " "
tva = ans.split()
for s in range(len(tva)):
    print(tva[s])
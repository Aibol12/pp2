a= int(input())
res = ""
for i in range(a):
    b = (input())
    if "@" in b:
        tv = b.split("@")
        if tv[1] == "gmail.com":
            res += tv[0] + " "
tva = res.split()
for s in range(len(tva)):
    print(tva[s])
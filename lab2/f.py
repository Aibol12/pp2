dict={}
listnames=[]
for i in range(int(input())):
    txt=input().split()
    name=txt[0]
    amount=int(txt[1])
    if name in dict:
        dict[name]=dict[name]+amount
    else:
        dict[name]=amount
        listnames.append(name)
Max=0
listnames.sort()
for i in dict:
    if dict[i]>Max:
        Max=dict[i]
for name in listnames:
    if dict[name]==Max:
        print(f'{name}',"is lucky!")
    else:
        print(f'{name}',"has to receive", f'{Max-dict[name]}', "tenge")
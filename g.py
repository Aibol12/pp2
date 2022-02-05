def Todecimal(x): 
    if x == 1 or x == 0:
        return x
    return x%10 + 2*Todecimal(x//10) 
a = int(input()) 
print(Todecimal(a))
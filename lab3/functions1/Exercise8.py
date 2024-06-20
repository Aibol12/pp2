def spy_game(list):
    c1=0
    c2=0
    c3=0
    for i in range(len(list)):
        if (list[i]==0 and c1==0):
            c1+=1
        if(list[i]==0 and c1==1 and c2==0):
            c2+=1
        if(list[i]==7 and c1==1 and c2==1):
            c3+=1
    print(str(c1)+str(c2)+str(c3))
    if(c1==1 and c2==1 and c3==1):
        return True
    return False
    

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
def un_wo_set(list):
    unique=[]
    for i in list:
        if i not in unique:
            unique.append(i)
    print(unique)
un_wo_set([1,2,4,0,0,7,5])
un_wo_set([1,0,2,4,0,5,7])
un_wo_set([1,7,2,0,4,5,0])
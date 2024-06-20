def has_33(x):
    for i in range(len(x)-1):
        if x[i:i+2]==[3,3]:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 1,2,4,5,1,3,3]))
print(has_33([2,4,6,7,8]))
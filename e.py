def isPrime(a):
    if a == 2 or a == 3 :
        return True
    if a%2 == 0 or a < 2 :
        return False
    for n in range(3, int(a) ,1):
        if a%n!=0:
            return True
    return False

x, y = [int(x) for x in input().split()]
if x < 500 and y%2==0 and isPrime(x):
    print('Good job!')
else :
    print('Try next time!')
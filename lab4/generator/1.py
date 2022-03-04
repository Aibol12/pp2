def g(n):
    for i in range (1, n+1, 1):
        x=pow(i, 2)
        yield x

n=int(input())
for i in g(n):
    print(i)

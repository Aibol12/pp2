def s(a, b):
    for i in range(a, b + 1):
        x = pow(i, 2)
        yield x
a, b = list(map(int, input().split()))
for i in s(a,b):
    print(i)
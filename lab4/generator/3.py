a = int(input())
def divided(n):
    for i in range(0, a):
        if i % 3 == 0 and i % 4 == 0 :
            yield i
for i in divided(a):
    print(i)
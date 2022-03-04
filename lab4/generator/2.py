def E(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i
n = int(input())
row = []
for i in E(n):
    row.append(i)
print(row)
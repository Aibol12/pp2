# Implement a generator that returns all numbers from (n) down to 0.

def reversive(n):
    for i in range(n, 0, -1):
        yield i 

n = int(input())

for rev in reversive(n):
    print(rev)
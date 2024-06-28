# Create a generator that generates the squares of numbers up to some number N.

def squares_until_n(n):
    for i in range(1, n+1):
        yield i**2   #generator lazy iterator, yield used to return iterator 
    
n = int(input())

for squares in squares_until_n(n):
    print(squares)
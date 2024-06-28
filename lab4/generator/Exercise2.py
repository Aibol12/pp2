# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def print_even_num(n):
    for i in range(0, n+1): #from zero to n
        if(i%2==0):
            yield i
 
n = int(input())

for evens in print_even_num(n):
    print(evens)
def histogram(numbers):
    for num in numbers:
        print('*' * num)
input_numbers = input()
numbers = [int(x) for x in input_numbers.split()]
histogram(numbers)

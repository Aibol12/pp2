with open('a.txt', 'r') as first:
    with open('b.txt', 'w') as second:
        for line in first:
            second.writelines(line)

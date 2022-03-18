with open('a.txt', 'w') as f:
    while True:
        x = input()
        if x == '0':
            break
        f.writelines([x, '\n'])

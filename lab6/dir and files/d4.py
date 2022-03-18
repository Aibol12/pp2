a = open('ex.txt', 'r')

cmd = 0
for i in a.readlines():
    cmd += 1
print(cmd)
a.close()

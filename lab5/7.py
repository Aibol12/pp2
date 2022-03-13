import re
a = input()
z = re.sub("['_']",' ',a)
x = re.sub("\s", '' ,z.title())
print(x)
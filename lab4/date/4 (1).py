from datetime import date
a = date(2008, 8, 18)
b = date(2008, 9, 26)
c = a - b
d = c*86400
print(d.days)
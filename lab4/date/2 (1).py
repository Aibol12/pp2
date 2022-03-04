from datetime import datetime, timedelta
a = datetime.today() - timedelta(1)
b = datetime.now()
c = datetime.today() + timedelta(1)
print(a.strftime("%A"))
print(b.strftime("%A"))
print(c.strftime("%A"))
#Write a Python program to print yesterday, today, tomorrow.

import datetime as dt

def yesterTomor():
    yesterday = dt.datetime.now() - dt.timedelta( days= 1)
    today = dt.datetime.now()
    tomorrow = dt.datetime.now() + dt.timedelta( days= 1)
    return [yesterday, today, tomorrow]


a, b, c = yesterTomor()
print( a, b, c)
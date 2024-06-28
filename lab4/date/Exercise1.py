#Write a Python program to subtract five days from current date.

import datetime as dt

def minus5days():
    return dt.datetime.now() - dt.timedelta( days= 5)


print( minus5days() )

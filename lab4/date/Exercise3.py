#Write a Python program to drop microseconds from datetime.

import datetime as dt

def dropMicroSec( date):
    newdate = date.replace( microsecond = 0)
    return newdate

data = dt.datetime( year = 2003, month = 1, day = 25, hour = 10, minute = 32, second= 56, microsecond= 123)
print (dropMicroSec(data))

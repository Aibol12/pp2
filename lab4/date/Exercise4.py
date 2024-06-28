#Write a Python program to calculate two date difference in seconds.

import datetime as dt
def dropMicroSec( date):
    newdate = date.replace( microsecond = 0)
    return newdate
data = dt.datetime( year = 2003, month = 1, day = 25, hour = 10, minute = 32, second= 56, microsecond= 123)

def diffenceSec( date1, date2):
    timedelta = dropMicroSec(date1)- dropMicroSec(date2)
    return abs(timedelta.total_seconds() )
print( diffenceSec( data, dt.datetime.now()))
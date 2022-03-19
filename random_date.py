import random
import time
from datetime import datetime
from dateutil import tz

START = "2008-09-20 00:00:00"
END = "2020-09-20 00:00:00"


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date():
    date = str_time_prop(START, END, '%Y-%m-%d %H:%M:%S', random.random())
    return date


print(random_date())

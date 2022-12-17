import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

import calendar

print(calendar.month(2002,5))
calendar.setfirstweekday(6)
print(calendar.month(2002,5,1,1))

print(calendar.isleap(2000))

print(calendar.calendar(2019))

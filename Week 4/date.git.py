#1
import datetime
ans=datetime.date.today()-datetime.timedelta(day=5)
print(ans)



#2

from datetime import date, timedelta
print(date.today() - timedelta(days=1))
print(date.today())
print(date.today() + timedelta(days=1))



#3

import datetime
ans = datetime.datetime.today().replace(microsecond=0)
print(ans)



#4
import datetime

d0 = datetime.datetime(2022, 6, 15, 12, 0, 0)
d1 = datetime.datetime(2022, 6, 18, 15, 30, 0)
delta = (d1 - d0).total_seconds()
print(delta)

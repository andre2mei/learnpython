from datetime import datetime
from datetime import timedelta
from datetime import date

today=date.today()
# Option A:
tomorrow=today+timedelta(days=1)
# Option B:
tomorrow2=date(today.year,today.month,today.day+1)

print(tomorrow)
print(tomorrow2)
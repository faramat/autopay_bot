import datetime

today = datetime.datetime.now()
date_pay = (int(today.timestamp()))
delta = datetime.timedelta(days=31)
date_end = today + delta
date_end = int(date_end.timestamp())


print(date_pay)
print(date_end)
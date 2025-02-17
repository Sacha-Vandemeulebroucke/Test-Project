import datetime


date = datetime.date(2025,2,14)
today_ = datetime.date.today()

time = datetime.time(12,30,5)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S  %m-%d-%Y")
print(date)
print(today_)
print(time)
print(now)

target_datetime = datetime.datetime(2026,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime > current_datetime:
    print("has passed")
else:
    print("has not passed")
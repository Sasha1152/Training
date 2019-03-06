import datetime
import time
import pytz

my_date = datetime.datetime.today()
print('my date: ', my_date)

now = datetime.datetime.now()
print('Now: ', now)

my_day = datetime.datetime.date(my_date)
print('my day: ', my_day)

my_time = datetime.datetime.time(my_date)
print('my time: ', my_time)

my_timestamp_mkr = datetime.datetime.timestamp(my_date)
print('my timestamp: ', my_timestamp_mkr)
print('my timestamp (int): ', int(my_timestamp_mkr))

print('sec (time.time): ', time.time())

sec = time.time()
print(time.ctime(sec))

start_date = '2019-01-30'
start_date_timestamp = time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d").timetuple())
print('start_date_timestamp: ', start_date_timestamp)

end_date = '2019-02-01'
end_date_timestamp = time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d").timetuple())
print('end_date_timestamp: ', end_date_timestamp)

tz = pytz.timezone("Europe/Kiev")
print(datetime.datetime.fromtimestamp(end_date_timestamp, tz))

print(datetime.datetime.today().weekday())

print(datetime.timedelta(days=1, hours=5))
print(datetime.date(2019, 1, 1))

print(my_date.replace(hour=0, minute=0, second=0, microsecond=0))

print(datetime.timedelta(seconds=60*10))

print(datetime.datetime.combine(my_date, my_time))

print(datetime.time(10, 0, 0))
print(datetime.date(2020, 2, 2))

my_time = datetime.time(10, 15, 30)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(datetime.datetime.combine(my_day, my_time))

print(datetime.datetime(10, 15, 30))

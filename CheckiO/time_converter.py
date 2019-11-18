# https://py.checkio.org/ru/mission/time-converter-24h-to-12h/

def time_converter(time):
    hour = int(time[:2])
    if hour == 0:
        return '12' + time[2:] + ' a.m.'
    elif hour < 12:
        return time[1:] + ' a.m.'
    elif hour == 12:
        return time + ' p.m.'
    else:
        hour = hour - 12
        time = str(hour) + time[2:] + ' p.m.'
        return time


print(time_converter('12:30'))
print(time_converter('09:00'))
print(time_converter('23:15'))
print(time_converter('00:30'))

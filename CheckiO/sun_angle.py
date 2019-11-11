# https://py.checkio.org/ru/mission/sun-angle/
from time import strptime


def sun_angle(time):
	strptime(time, '%H:%M')
	hours, minutes = (int(i) for i in time.split(':'))
	if strptime(time, '%H:%M') < strptime('6:00', '%H:%M')\
			or strptime(time, '%H:%M') > strptime('18:00', '%H:%M'):
		return "I don't see the sun!"
	else:
		min_to_angle = 180 / (12 * 60)
		total_minutes = (hours - 6) * 60 + minutes
		angle = min_to_angle * total_minutes
		return angle

print(sun_angle("07:00"))
assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75
assert sun_angle("01:23") == "I don't see the sun!"
assert sun_angle("21:41") == "I don't see the sun!"

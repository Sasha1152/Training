# https://www.geeksforgeeks.org/str-vs-repr-in-python/

import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))

print(ascii('Hello world'))  # 'Hello world'
print(ascii('Привіт'))  # '\u041f\u0440\u0438\u0432\u0456\u0442'
print(ascii(25))  # 25

print(str('hello'))
n = 5
a, b = 0, 1
while n >= 0:
   a, b = a + b, a
   n -= 1
   print a, b

print(b)
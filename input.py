import math
print('x^3+sin(y)=?')
x = float(input('x='))
y = float(input('y='))
print('x^3+sin(y)=', math.pow(x, 3) + math.sin(y))
print('pi=', math.pi)
print('---' * 3)

# For Python 2:
# n = raw_input('n=')  # type: 2 + 3
# print n  # 2 + 3
#
# n = input('n=')  # type: 2 + 3
# print n  # 5

# For Python 3:
n = input('n=')  # type: 2 + 3
print(n)  # 2 + 3

n = eval(input('n='))  # type: 2 + 3
print(n)  # 5
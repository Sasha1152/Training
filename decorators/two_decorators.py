def square(func):
    return lambda x: func(x * x)

def addsome(func):
    return lambda x: func(x + 1)


@square  # calls first
@addsome  # cals second
def identity(x):
    return x

print(identity(2)) # 5


@addsome
@square
def identity(x):
    return x

print(identity(2))  # 9

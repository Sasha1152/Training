def square(func):
    return lambda x: func(x * x)

def add_one(func):
    return lambda x: func(x + 1)


@square  # calls first
@add_one  # calls second
def identity(x):
    return x

print(identity(2)) # 5


@add_one
@square
def identity(x):
    return x

print(identity(2))  # 9

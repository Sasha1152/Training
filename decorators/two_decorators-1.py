def dec1(func):
    def wrap(*args):
        print('dec1 called')
        return func(*args)
    return wrap


def dec2(func):
    def wrap(*args):
        print('dec2 called')
        return func(*args)
    return wrap


@dec1  # calls first
@dec2  # cals second
def identity1(x):
    return 'identity1 called, result: ' + str(x)

print(identity1(1))


@dec2
@dec1
def identity2(x):
    return 'identity2 called, result: ' + str(x)

print(identity2(2))

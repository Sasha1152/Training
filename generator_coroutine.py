def grep(pattern):
    print(f"Looking for letter '{pattern}'")
    while True:
        line = yield
        if pattern in line:
            print(line)

gen = grep("A")
next(gen)
gen.send('eiufeagergwer')

gen.send('egfeggAgegwer')

###################### or using the decorator:
print('----' * 3)

import functools

def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def grep(pattern):
    print(f"Looking for letter '{pattern}'")
    while True:
        line = yield
        if pattern in line:
            print(line)

gen = grep("B")
gen.send('eiufeagergwer')
gen.send('egfBeggAgegwer')

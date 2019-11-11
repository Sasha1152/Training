def compose(f, g):
    return lambda x: f(g(x))

def double(x):
    return x * 2

def inc(x):
    return x + 1

inc_and_double = compose(double, inc)
print(inc_and_double(3))
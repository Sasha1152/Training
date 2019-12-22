import functools

def runcounter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = 0
    return wrapper

@runcounter
def identity(x):
    return x

identity(10)
identity(20)
identity(30)
print(identity.ncalls)  # 3
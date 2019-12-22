import functools
from datetime import time


def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
    print(func.__name__, end=" ... ")
    acc = float("inf")
    for i in range(n_iter):
        tick = time.perf_counter()
        result = func(*args, **kwargs)
        cc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner


import functools


@functools.lru_cache(maxsize=16)
def identity(x):
    return x

identity(1)
identity(1)
identity(1)
identity(1)
identity(1)
print(identity.cache_info())


def func(n):
    """
    >>> func(5)
    [0, 1, 2, 3, 4]
    >>> func(12)
    ... # doctest: +NORMALIZE_WHITESPACE
    [0, 1,    2,     3, 4, 5,
    6, 7, 8,     9, 10, 11]
    >>> func(100)
    ... # doctest: +ELLIPSIS
    [0, 1, 2, 3, 4, 5, ...]
    >>> func(500)
    ... # doctest: +ELLIPSIS
    [0, 1, 2, 3, ... 54, 55, ... 498, 499]
    """
    return [i for i in range(n)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
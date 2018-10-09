def purse_number(num):
    """
    >>> print(purse_number(34567))
    {'odd': 3, 'even': 2}
    >>> print(purse_number(100))
    {'odd': 1, 'even': 2}
    >>> print(purse_number('word'))
    False
    """
    if type(num) is str:
        return False

    counter = {'odd': 0, 'even': 0}
    num_str = str(num)
    for i in num_str:
        if int(i) % 2 == 0:
            counter['even'] += 1
        else:
            counter['odd'] += 1
    return counter

print(purse_number(34567))
def count(sub,s):
    '''
    >>> count('is', 'Mississippi')
    2
    >>> count('an', 'banana')
    2
    >>> count('ana', 'banana')
    2
    >>> count('nana', 'banana')
    1
    >>> count('nanan', 'banana')
    0
    '''
    index = 0
    n = 0
    for letter in s:
        word = s[index:len(sub) + index]
        index += 1
        if word == sub:
            n += 1
        # print(word)
    return n

if __name__ == '__main__':
    import doctest
    doctest.testmod()

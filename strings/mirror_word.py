def mirror(s):
    '''
    >>> mirror('good')
    'gooddoog'
    >>> mirror('yes')
    'yessey'
    >>> mirror('python')
    'pythonnohtyp'
    '''
    result = ''
    for letter in s:
        result = letter + result
    result = s + result
    return result
def reverse(s):
    """
    >>> reverse('happy')
    'yppah'
    >>> reverse('python')
    'nohtyp'
    """

    rev = ''
    for letter in s:
        rev = letter + rev
    return rev

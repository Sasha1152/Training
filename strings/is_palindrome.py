def is_palindrome(s):
    '''
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab')
    False
    >>> is_palindrome('tenet')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('straw warts')
    True
    '''
    rewerse_word = ''
    for letter in s:
        rewerse_word = letter + rewerse_word
        # print(rewerse_word)
    return(rewerse_word == s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

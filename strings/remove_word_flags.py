def remove(sub,s):
    '''
    >>> remove('cde', 'abcdefg')
    'abfg'
    >>> remove('an', 'banana')
    'ba'
    >>> remove('cyc', 'bicycle')
    'bile'
    >>> remove('iss', 'Mississippi')
    'Mippi'
    >>> remove('egg', 'bicycle')
    'bicycle'
    '''
    index = 0
    new_word = ''
    while index < len(s):
        flag = True
        variable_word = s[index:len(sub) + index]
        
        if variable_word == sub:
            # print('*')
            index = index + len(sub)
            flag = False
        
        if flag == True:                                         
            new_word = new_word + s[index]
            index += 1
        # print(new_word)
    return new_word

if __name__ == '__main__.py':
    import doctest
    doctest.testmod()

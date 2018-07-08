a = 'aeuioy'
def remover(text):
    '''
    >>> remover('apple')
    'ppl'
    >>> remover('juise')
    'js'
    '''
    result = ''
    for letter in text:
        if letter not in a:
            result = result + letter
    return result
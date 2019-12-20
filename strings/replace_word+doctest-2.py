def replace(s, old, new):
    """
    >>> replace('Ukraine', 'i', 'I')
    'UkraIne'
    >>> s = 'I love summer! summer is my favorite time of year!'
    >>> replace(s, 'summer', 'winter')
    'I love winter! winter is my favorite time of year!'
    >>> replace(s, 'o', 'a')
    'I lave summer! summer is my favarite time af year!'
    """
    sentence = s.split()
    sentence_list = []
    if len(sentence) == 1:
        for letter in s:
            if letter == old:
                sentence_list.append(new)
            else:
                sentence_list.append(letter)
        return (''.join(sentence_list))
    else:
        for word in sentence:
            if word == old:
                sentence_list.append(new)
            else:
                sentence_list.append(word)
        return (' '.join(sentence_list))
#    print(words)
'''
    if __name__ == '__main__.py':
        import doctest
        doctest.testmod()
'''        
print(replace('Ukraine', 'i', 'I'))
print()
replace('Ukraine ivo init', 'i', 'I')

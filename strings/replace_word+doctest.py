def replace(s, old, new):
    """
    >>> replace('Ukraine', 'i', 'I')
    'UkraIne'
    >>> s = 'I love summer! summer is my favorite time of year!'
    >>> replace(s, 'summer', 'winter')
    'I love winter! winter is my favorite time of year!'
    >>> replace(s, 'o', 'a')
    'I lave summer! summer is my favorite time af year!'
    """
    sentence = s.split()
    if len(sentence) == 1:
        for letter in sentence[0]:
            if letter == old:
                print(new, end='')
            else:
                print(letter, end='')
                
    else:
        for word in sentence:
            for letter in word:
                if letter == old:
                    print(new, end='')
            else:
                print(letter, end='')
                
#    print(words)

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

replace('Ukraine', 'i', 'I')
replace('Ukraine ivo init', 'i', 'I')

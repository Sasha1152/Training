import doctest

def replace(s, old, new):
    """
    >>> replace('Ukraine', 'i', 'I')
    'UkraIne'
    >>> replace('I love summer! summer is', 'summer', 'winter')
    'I love winter! winter is'
    """
    result = ''
    
    index = 0
    flag = False
    
    for letter in s:
        sliced_text = s[index:len(old) + index]
        print('Iteration ' + str(index))
        
        if flag == True:
            skip_counter -= 1
            if skip_counter == 0:
                flag = False
        
        if sliced_text == old:
            flag = True
            skip_counter = len(old)
            result += new
        elif flag == False:
            result += letter
            
        index += 1
    
    return result


if __name__ == '__main__':
    doctest.testmod()

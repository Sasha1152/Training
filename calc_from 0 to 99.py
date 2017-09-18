print 'Hello. This program is calculator'
print '*' * 30
while True:
    
    first_number = ''
    while type(first_number) is not float:
        try:
            first_number = float(raw_input( 'enter first number (from 0 to 99): '))
        except ValueError:
            print('Incorrect number')
            continue
        else:
            break
        
    sign = ''
    while True:
        sign = raw_input('Enter sumbol (+, -, *, /): ')
        if sign in [ '+','-','*','/']:
            break
        else:
            print('Incorrect sumbol')
            continue

    second_number = ''
    while type(second_number) is not float:
        try:
            second_number = float(raw_input( 'enter second number (from 0 to 99): '))
        except ValueError:
            print('Incorrect number')
            continue
        else:
            break
            
    if first_number < 0 or first_number >= 100:
        raise NameError('you entered wrong first number!')
    if second_number < 0 or second_number >= 100:
        raise NameError('you entered wrong second number!')    
    if sign == '+':
        result = first_number + second_number
    elif sign == '-':
        result = first_number - second_number
    elif sign == '*':
        result = first_number * second_number
    elif sign == '/':
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            print 'No division by zero allowed'
        else:
             print result
        finally:
            print 'Analysis'
    if sign == '+' or sign == '-' or sign == '*':
        print result
        
    print('Would you like to continue?')
    answer = raw_input('Press any key if YES, enter "exit" if NO: ')
    if answer == 'exit':
        break

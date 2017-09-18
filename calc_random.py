def random_action(first_number, second_number):
    import random
    first_number = int(first_number)*2
    second_number = int(second_number)
    sign = random.choice('+-*/')
    
    def print_answer():
        print('The result of ' + action + ' numbers ' + str(first_number) + ' and ' + str(second_number) + ' is number ' + str(result))
        
    if sign == '+':
        action = 'adding'
    elif sign == '-':
        action = 'substracting'
    elif sign == '*':
        action = 'multiplying'
    elif sign == '/':
        action = 'dividing'
    
    if sign == '+':
        result = first_number + second_number
        print_answer()
    elif sign == '-':
        result = first_number - second_number
        print_answer()
    elif sign == '*':
        result = first_number * second_number
        print_answer()
    elif sign == '/':
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            print 'No division by zero allowed'
        else:
             print_answer()
      
    print('The end')
random_action(89,9)

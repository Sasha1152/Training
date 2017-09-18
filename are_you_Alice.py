name = raw_input('Hello. What is your name?  ')
answer_1 = 'You are neither Alice, nor a little kid!'
if name == 'Alice':
    print('Hi, Alice!')

elif name == '':
    name = 'Mister X'  # Default name
    age = raw_input('How old are you?  ')
    if age == '':
        age = 20  # Default age
        print(answer_1)
    elif int(age) < 12:
        print('You are not Alice, kid!')
    else:
        print(answer_1)
        
else:
    age = raw_input('How old are you?  ')
    if age == '':
        age = 20  # Default age
        print(answer_1)
    elif int(age) < 12:
        print('You are not Alice, kid!')
    else:
        print(answer_1)

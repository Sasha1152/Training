name = ''
while True:
    print('Who are you?')
    name = raw_input('Enter your name: ')
    if name != 'Joe':
        continue
    else:
        print('Your password:')
        password = raw_input()
        if password == 'fish':
            break
print('Acces granded')
# https://py.checkio.org/ru/mission/roman-numerals/

print('Hello. This program converts Arabic numerals in Rome.')
print('*'*25)
while True:
    try:
        a =int(input('enter a number from 1 to 10, press any key to exit: '))
        length = len(str(a))
    except SyntaxError:
        break
    except NameError:
        break
    if a >= 1 and a<=3: print('I' * a)
    elif a == 4: print('IV')
    elif a == 5: print('V')
    elif a > 5 and a < 9: print('V'+'I'*(a - 5))
    elif a == 9: print('IX')
    elif a == 10: print('X')
    print('Do you want to continue?')
    

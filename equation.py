"""
this program solve a simple equation such as :
x + 5 = 15, 45 / x = 8 etc. A numbers must be
natural.
"""
while True:
    print('enter equation(type "exit" to quit):')
    s_start = str(input())
    if s_start == 'exit':
        break

    s = s_start.split()

    for i in range(0, 6, 2):
        try:
            s[i] = int(s[i])
            if i < 3:
                known = s[i]
            else:
                result = s[i]
        except ValueError:
            if i == 0 or 2:
                unknown = s[i]
            else:
                continue

    if s[1] == '+':
        x = result - known
        antisign = '-'

    elif s[1] == '*':
        x = result / known
        antisign = '/'

    elif s[1] == '-':
        if s[0] == unknown:
            x = result + known
            antisign = '+'
        elif s[2] == unknown:
            x = known - result
            antisign = '-'

    elif s[1] == '/':
        if s[0] == unknown:
            x = result * known
            antisign = '*'
        elif s[2] == unknown:
            x = known / result
            antisign = '/'

    for i in range(5):
        if s[i] == unknown:
            s[i] = str(x)
        else:
            s[i] = str(s[i])

    if (s[1] == '-' or s[1] == '/') and s[2] == str(x):
        print('{} = {} {} {}'.format(unknown, known, antisign, result))
    else:
        print('{} = {} {} {}'.format(unknown, result, antisign, known))

    print('{} = {}'.format(unknown, x))
    print( '-'*12)
    print(' '.join(s))

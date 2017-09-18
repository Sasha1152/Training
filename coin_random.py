import random
while True:
    def coin():
        x = random.random()
        if x > 0.5:
            return 0
        else:
            return 1
    print(coin())
    print('do you want to continue?')
    answer = raw_input('press any key if YES, press "n" if NO: ')
    if answer == 'n':
        break

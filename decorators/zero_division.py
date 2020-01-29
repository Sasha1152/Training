def decorator(function):
    def trying(*args):
        try:
            function(*args)
        except ZeroDivisionError:
            print(f"{args[0]} / 0 = It's imposible")
        else:
            print('DONE!')
    return trying

@decorator
def division(a, b):
    result = a / b
    print('{} / {} = {}'.format(a, b, result))

division(255, 5)
division(255, 0)
division(25, 4)
division(255, 0)

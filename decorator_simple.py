def decorator_1(function):
    def wrapper():
        print('*** code before function ***')
        function()
        print('*** code after function ***')
    return wrapper

def show():
    print('*** simple function "show" ***')

show()
print ('-'*25)

dec = decorator_1(show)
dec()
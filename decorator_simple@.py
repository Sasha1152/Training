def decorator_1(function):
    def wrapper():
        print('*** code before function #1 ***')
        function()
        print('*** code after function #1 ***')
    return wrapper

def decorator_2(function):
    def wrapper():
        print('*** code before function #2 ***')
        function()
        print('*** code after function #2 ***')
    return wrapper

@decorator_1
@decorator_2
def show():
    print('*** simple function "show" ***')
show()

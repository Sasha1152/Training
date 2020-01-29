def retry_division(retries):
    def decorator(function):
        def trying(*args, **kwargs):
            attempt = retries
            while attempt > 0:
                try:
                    function(*args, **kwargs)
                except ZeroDivisionError:
                    attempt -= 1
                    print(f"{args[0]} / 0 = It's imposible")
                else:
                    attempt = 0
                    return function
        return trying
    return decorator

@retry_division(retries = 4)
def division(a, b):
    result = a / b
    print('{} / {} = {}'.format(a, b, result))

division(25, 5)
division(1, 0)
division(20, 4)
division(2, 0)
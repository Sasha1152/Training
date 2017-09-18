def simple_decorator(fn):
    def decorate():
        print("before")
        print(fn())
        print("after")
    return decorate


@simple_decorator
def func():
    return "execute func()"

func()

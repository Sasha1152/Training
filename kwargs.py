def func1(*args):
    print(args)

func1(1, 2, 3)   # (1, 2, 3) - tuple


def func2(**kwargs):
    print(kwargs)

func2(a=1, b=2, c=3)  # {'a': 1, 'c': 3, 'b': 2} - dict


def func3(a, b, c):
    print a, b, c

func3(**{'a': 1, 'c': 3, 'b': 2})  # a c b 1 3 2


def func4(**kwargs):
    for i in kwargs:
        print i

kwargs = {'a': 1, 'b': 2, 'c': 3}
func4(**kwargs)

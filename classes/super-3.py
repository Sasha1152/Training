# https://www.journaldev.com/15911/python-super

class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, n):
        print('Printing from class A :', n)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, n):
        print('Printing from class B :', n)
        super().sub_method(n + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, n):
        print('Printing from class C :', n)
        super().sub_method(n + 1)


c = C()
c.sub_method(1)

help(C)

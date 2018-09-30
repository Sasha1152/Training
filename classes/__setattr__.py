class A:
    def __init__(self, v):
        self.field1 = v

a = A(10)
a.field2 = 20  # not recommended
print(a.field1, a.field2)  # 10 20

class A:
    def __init__(self, v):
        self.field1 = v

    def __setattr__(self, attr, value):
        if attr == 'field1':
            self.__dict__[attr] = value
        else:
            raise AttributeError

a = A(10)
# a.field2 = 20 # AttributeError
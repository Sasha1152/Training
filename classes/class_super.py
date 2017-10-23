class A(object):
    """Simple docstring"""
    a = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        pass

    def pri(self):
        print 'Hello!'


class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name)
        self.age = age

husband = A('Sasha')
print husband.name

wife = B('Kate', '30')
print wife.name, wife.age

husband.pri()
wife.pri()
print A.a
A.a = 1
print B.a
print A.__doc__
print A.__init__
print B.__dict__

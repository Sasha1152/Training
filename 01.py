class A(object):
    def __init__(self, name):
        self.name = name


class B(A):
    def __init__(self, name, age):
        super(A, self).__init__(name)
        self.age = age

one = A('Sasha')
print one.name

two = B('Kate', '12')
print two.age
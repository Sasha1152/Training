class A(object):
    def __init__(self, name):
        self.name = name

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
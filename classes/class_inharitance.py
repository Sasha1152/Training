class A1:
    def fb(self):
        print "class1"

class A2:
    def fb(self):
        print "class2"

class B(A1, A2):
    def f(self):
        self.fb()

b=B()
b.fb()
# print B.__mro__
class X(object):
    def who_am_i(self):
        print("I am a X")

class Y():
    def who_am_i(self):
        print("I am a Y")

class A(X, Y):
    def who_am_i(self):
        print("I am a A")

class B(Y, X):
    def who_am_i(self):
        print("I am a B")

class F(A, B):
    def who_am_i(self):
        print("I am a F")

f = F()
f.who_am_i()
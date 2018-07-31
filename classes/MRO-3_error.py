class X(object):
    # def who_am_i(self):
    #     print("I am a X")
    pass

class Y():
    # def who_am_i(self):
    #     print("I am a Y")
    pass

class A(X, Y):
    # def who_am_i(self):
    #     print("I am a A")
        pass

class B(Y, X):
    # def who_am_i(self):
    #     print("I am a B")
    pass

class F(A, B):
    def who_am_i(self):
        print("I am a F")

f = F()
f.who_am_i()

"""
    X   Y  Y   X
     \ /    \ /
      A      B
       \    /
        \  /
         F
"""
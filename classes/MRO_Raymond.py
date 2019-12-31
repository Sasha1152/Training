# https://www.youtube.com/watch?v=61UuKJRl2m0&feature=youtu.be

class A:
    def get_classname(self):
        return 'A'

class B(A):
    pass

class C(A):
    def get_classname(self):
        return 'C'

class D(B, C):
    pass

print(A().get_classname())  # A
print(B().get_classname())  # A
print(C().get_classname())  # C
print(D().get_classname())  # C

help(D)
print(D.__bases__)
"""
  A
 / \
B   C
 \ /
  D
D -> B -> С -> A
"""
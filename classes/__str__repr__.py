class A:
    def __str__(self):
        return "This is object of A"

a = A()
print(a)
print(str(a))
print(repr(a))

print('-----')

class B:
    def __repr__(self):
        return "This is object of B"

b = B()
print(b)
print(str(b))
print(repr(b))
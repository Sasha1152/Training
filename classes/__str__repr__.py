class A:
    def __str__(self):
        return "This is object of A"

a = A()
print(a)  # This is object of A
print(str(a))  # This is object of A
print(repr(a))  # <__main__.A object at 0x7f6dd451f040>

print('-----')

class B:
    def __repr__(self):
        return "This is object of B"

b = B()
print(b)  # This is object of B
print(str(b))  # This is object of B
print(repr(b))  # This is object of B

print('---'*3)
######################################

class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def __repr__(self):
        return "Counter({})".format(self.value)

    def __str__(self):
        return "Counted to {}".format(self.value)

c = Counter(42)
print(c)  # Counted to 42
print(repr(c))  # Counter(42)

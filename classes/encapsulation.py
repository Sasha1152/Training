class B:
    __count = 0

    def __init__(self):
        B.__count += 1

    def __del__(self):
        B.__count -= 1

    @classmethod
    def get_object(cls):
        return B.__count

print(B._B__count)  # 0
a = B()
# print(B.__count) # error
print(a._B__count)  # 1
b = B()
print(b._B__count)  # 2
print(b.get_object())  # 2
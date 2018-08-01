class B:
    __count = 0

    def __init__(self):
        B.__count += 1

    def __del__(self):
        B.__count -= 1

    @classmethod
    def get_object(cls):
        return B.__count


a = B()
# print(B.__count) # error
print(B._B__count)
b = B()
print(B._B__count)
print(B.get_object())
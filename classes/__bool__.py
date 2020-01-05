class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def __bool__(self):
        # return bool(self.value)
        return bool(0)

c = Counter(42)
print(bool(c))
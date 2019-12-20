def cell(value=None):
    def fget():
        return value
    def fset(update):
        nonlocal value
        value = update
    return fget, fset

myget, myset = cell()
print(myset(42))  # None
print(myget())  # 42

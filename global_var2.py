var = 1

def foo():
    # global var
    var = 2
    return var

print(var)
foo()
print(var)
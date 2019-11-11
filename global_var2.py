var = 1

def foo():
    # global var
    var = 2
    print(var)

print(var)
foo()
print(var)

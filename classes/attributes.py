class Simple(int):
    atrr = 100


a = Simple(1)
print(a.__dict__)  # {}
print(Simple.__dict__)

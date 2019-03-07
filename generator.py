generator_1 = (x * x for x in range(3))  # Simple generator
print(generator_1)  # <generator object <genexpr> at 0x022A7198>
for i in generator_1:
    print(i)  # 0 1 4


def generator_2():
    for i in (1, 2, 3):
        yield i

g = generator_2()  # create generator
print(g)  # <generator object generator at 0x022B7198>
for i in g:
    print(i)  # 1 2 3
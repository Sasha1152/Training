from random import randint
def test(n):
    import pdb; pdb.set_trace()
    f = randint(1, n)
    return f*2

print(test (2))
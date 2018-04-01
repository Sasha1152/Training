sum([[1,2], [3,4], [5, 6]], [])  # [1, 2, 3, 4, 5, 6]

all([True,False,True])  # False

any([True,False,True])  # True

max(['vi','linux','win'], key = lambda x: len(x))  # linux

c = ['a', 'b', 'c']
d = [1, 2, 3]
print(zip(c,d))  # [('a', 1), ('b', 2), ('c', 3)]

d = [1, 2, 3]
map(lambda x: x*2, d)  # [2, 4, 6]

map(lambda a, b, c: a + b + c,
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6])  # [6, 9, 12, 15]

map(None,
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6,10])
# [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (None, None, 10)]

d = [1, 2, 3]
reduce(lambda x, y: x + y, d)  # 6

list(enumerate(['a','b','c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]

filter(lambda x: x % 2, [1,2,3,4,5,6] )  # [1, 3, 5]

a = 7
def f():
    global a
    a -= 1
    return a
print list(iter(f, 2))  # [6, 5, 4, 3]

list(xrange(5))  # [0, 1, 2, 3, 4]

tuple(xrange(5))  # (0, 1, 2, 3, 4)

print iter('abcdef').next()  # a

sorted('bca')  # ['a', 'b', 'c']
sorted('bca',reverse = True)  # ['c', 'b', 'a']
sorted(['win','linux','vi'], key = lambda x: len(x))  # ['vi', 'win', 'linux']
sorted([['a',3], ['b',1], ['c',2]], cmp = lambda a, b: cmp(a[1], b[1]))
     # [['b', 1], ['c', 2], ['a', 3]]

print range(10)[slice(0, 7, 2)]  # [0, 2, 4, 6]
print 'abcdefghqwrtyuiop'[slice(0, 10, 2)]  # 'acegq'

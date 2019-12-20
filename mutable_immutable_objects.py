# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

x = 10
y = x

print('p1:', id(x), x)
print('p2:', id(y), y)
print('p3:', id(10))

x = x + 1

print('p4:', id(x), x)
print('p5:', id(y), y)
print('---'*3)


m = list([1, 2, 3])
n = m

print('p6:', id(m), m)
print('p7:', id(n), n)
print('p8:', id([1, 2, 3]))

m.append(4)

print('p9:', id(m), m)
print('p10:', id(n), n)
print('---'*3)


def update_list(list1):
    list1 += [3]

n = [1, 2]

print('p11:', id(n), n)
update_list(n)
print('p12:', id(n), n)
print('---'*3)


def update_number(n):
    print('pfunc:', id(n), n)
    n += 10

b = 5
print('p16:', id(b), b)
update_number(b)
print('p17:', id(b), b)

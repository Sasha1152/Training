import dis

print(dis.dis("first, *rest, last = ('a', 'b', 'c')"))
print(dis.dis("first, *rest, last = ['a', 'b', 'c']"))
print(dis.dis('a = 1'))

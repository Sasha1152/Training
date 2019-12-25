from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("George", age=77)

print(p)
print(p._fields)
print(p.name, p.age)
print(p._asdict())

p2 = p._replace(name="Bill")
print(p)
print(p2)

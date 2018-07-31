class A:
    def __init__(self, name):
        self.name = name

    def pri(self):
        return 'Hello!'

husband = A('Sasha')

print(husband.name)
husband.name2 = 'Alex'
print(husband.name2)
print(husband.pri())
# the same:
print(A.pri(husband))

class A:
    def __init__(self, name):
        self.name = name

    def pri(self):
        return 'Hello!'

husband = A('Sasha')

print(husband.name)
print(husband.pri())
# the same:
print(A.pri(husband))

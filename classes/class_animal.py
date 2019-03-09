class Animal:
    attribute = 'OK'
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name


a = Cat('as')

print(Cat('boo').attribute)

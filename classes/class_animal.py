class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return 'Woof, woof'

animals = [Cat('Missy'), Cat('Jack'), Cat('Lassie')]
for animal in animals:
    print (animal.name + ': ' + animal.talk())

print(Dog('Butcher'))
print(Dog('Butcher').name)
print(Dog('Butcher').talk())
print(Dog('Butcher').talk)
print(Cat('Missy').name)
print(Cat)
print('----')
abstr = Animal('Zorro')
print(abstr.talk())
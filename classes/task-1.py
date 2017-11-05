""" the task see the book 'Simple Python' - Bill Lubanovich p.178 """

class Thing():
    pass

print(Thing())
obj1 = Thing()
print(obj1)

class Thing2():
    letters = 'abc'

print(Thing2.letters)

class Thing3():
    pass

Thing3.letters = 'xyz'
print(Thing3.letters)

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    # def __str__(self):
    #     return self.name + '_' +\
    #            self.symbol + '_' +\
    #            str(self.number)

    @property
    def name(self):
        return self.__name

obj_elem = Element('Hydrogen', 'H', 1)
hydro_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
obj_hydrogen = Element(**hydro_dict)
print(obj_hydrogen._Element__symbol)
# print(obj_hydrogen.dump())
print(obj_hydrogen.name)

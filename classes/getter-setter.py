class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)

obj = Duck('Howard')
print(obj.name)
# the same:
# print obj.get_name()
obj.name = 'Donald' # inside the setter
# the same:
# obj.set_name('Donald')
print(obj.name)

print('----'*3)
########################### or the same with deleter:

class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    @name.deleter
    def name(self):
        print('inside the deleter')
        del self.hidden_name

obj = Duck('Howard')
print(obj.name)  # inside the getter Howard
print(obj.__dict__)  # {'hidden_name': 'Howard'}
obj.name = 'Donald'  # inside the setter
print(obj.name)  # inside the getter Donald
print(obj.hidden_name)  # Donald
print(obj.__dict__)  # {'hidden_name': 'Donald'}
del obj.name  # inside the deleter
# print(obj.name)  # AttributeError: 'Duck' object has no attribute 'hidden_name'

print('----'*3)
########################### or with hidden attribute:

class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

obj = Duck('Howard')
print(obj.name)  # inside the getter Howard
obj.name = 'Donald'  # inside the setter
print(obj.name)  # inside the getter Donald
# obj.__name # AttributeError: 'Duck' object has no attribute '__name'
print(obj.__dict__)  # {'_Duck__name': 'Donald'}
print(obj._Duck__name)  # Donald

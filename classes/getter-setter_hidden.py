""" for Python 3"""


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
print(obj.name)
obj.name = 'Donald'  # inside the setter
print(obj.name)
# obj.__name # AttributeError: 'Duck' object has no attribute '__name'
print(obj._Duck__name)

class Duck():
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
obj.na = 'Donald'
# the same:
# obj.set_name('Donald')
print(obj.na)


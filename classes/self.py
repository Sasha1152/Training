class A:
    def __init__(self, name):
        self.name = name

    def say(self):
        return 'Hello!'

husband = A('Sasha')

print(husband.name)  # Sasha
husband.name2 = 'Alex'
print(husband.name2)  # Alex
print(husband.say())  # Hello!
# the same:
print(A.say(husband))  # Hello!

class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.lower()

    # def __str__(self):
    #     return "it's str " + self.text

    def __repr__(self):
        return "it's repr " + self.text

obj1 = Word('ha')
obj2 = Word('HA')
obj3 = Word('eh')

print(obj1.text)
print(obj1.equals('Ha'))
print(obj1.equals('hA'))
print(obj1)
print(obj2)
print(obj3)
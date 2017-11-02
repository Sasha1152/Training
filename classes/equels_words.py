class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

obj1 = Word('ha')
odj2 = Word('HA')
obj3 = Word('eh')

obj1.equals(obj2)
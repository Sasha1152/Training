class Boo(int):
    a = []

    def add(self):
        self.a.append(1)

b = Boo()
b.add()
print(b.a)  # [1]

b2 = Boo()
print(b2.a)  # [1]
print('----'*3)

###########################

class Auu:
    def __init__(self, num):
        self.num = num
        self.a = []

    def add(self):
        self.a.append(self.num)

auu = Auu(1)
auu.add()
print(auu.a)  # [1]

auu2 = Auu(2)
print(auu2.a)  # []
auu2.add()
print(auu2.a)  # [2]

class Based:
    def __init__(self, n):
        self.n = n

    def out(self):
        print(self.n)


class One(Based):
    def multi(self, m):
        self.n *= m


class Two(Based):
    def inlist(self):
        self.inlist = list(str(self.n))

    def out(self):
        print(self.inlist)


obj1 = One(12)
obj1.multi(10)
obj1.out()

obj2 = Two(123)
obj2.inlist()
obj2.out()

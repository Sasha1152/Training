class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print('I am a class "A"!')

    @classmethod
    def kids(cls):
        print('class "A" has', cls.count, 'objects')  # or (A.count) - the same

obj1 = A()
obj2 = A()
obj3 = A()

A.kids()  # 3  - attribute of class
obj1.kids()  # 3  - attribute of object
obj1.exclaim()  # I'm an A!  - only attribute of object
# A.exclaim() # TypeError: unbound method exclaim()
             # must be called with A instance as
             # first argument (got nothing instead)

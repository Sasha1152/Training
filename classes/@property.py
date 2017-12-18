class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 6
print(c.diameter)
c = Circle(8)
print(c.diameter)
# c.diameter = 1 # AttributeError: can't set attribute

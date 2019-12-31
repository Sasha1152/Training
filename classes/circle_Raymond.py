# https://www.youtube.com/watch?v=tfaFMfulY1M&feature=youtu.be
import math

class Circle:
    """An advanced circle analitic toolkit"""

    __slots__ = ['diameter']  # flyweight design pattern suppresses the instance dictionary
    version = '0.1'  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

    @property                 # convert dotted access to method calls
    def radius(self):
        """Radius of a circle"""
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2



    def area(self):
        """Perform quadrature on a shape of uniform radius"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod                 # alternative constructor
    def from_bbd(cls, bbd):
        """Construct a circle form a bounding box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # or Circle(radius)

    @staticmethod                # attach functions to classes
    def angle_to_grade(angle):
        """Convert angle in degree to a percentage grade"""
        return math.tan(math.radians(angle)) * 100


cuts = [0.1, 0.5, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print(
        f'A circlet with a radius of {c.radius}\n'
        f'has a perimeter {c.perimeter()}\n'
        f'and a cold area of {c.area()}'
    )
    c.radius *= 1.1  # attribute was changed!
    print(f'and a warm area of {c.area()}\n')


с = Circle.from_bbd(25.1)
print(
    f'A circlet with a bbd of 25.1\n'
    # f'has a radius {c.radius()}\n'  # TypeError: 'float' object is not callable
    f'and an area of {c.area()}\n'
    )


class Tire(Circle):
    """Tires are circles with a corected perimeter"""

    def perimeter(self):
        """Circumference corrected for rubber"""
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print(
    f'A tire of radius {t.radius}\n'
    f'has an inner area of {t.area()}\n'
    f'and an odometer corrected perimeter of {t.perimeter()}'
)

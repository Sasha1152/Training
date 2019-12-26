# https://www.youtube.com/watch?v=tfaFMfulY1M&feature=youtu.be
import math

class Circle:
    """An advanced circle analitic toolkit"""

    version = '0.1'  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

    def area(self):
        """Perform quadrature on a shape of uniform radius"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2.0 * math.pi * self.radius


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

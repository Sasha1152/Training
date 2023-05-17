# https://py.checkio.org/ru/mission/oil-pie/

from fractions import Fraction


def divide_pie(groups):
    n = sum(abs(i) for i in groups)  # quantity of robots
    pie = Fraction(1, 1)

    for i in groups:
        if i > 0:
            pie = pie - Fraction(i, n)
        elif i < 0:
            pie = pie - pie * Fraction(abs(i), n)

    return pie.numerator, pie.denominator


print(divide_pie((2, -1, 3)))
print(divide_pie((10,)))
print(divide_pie((-1, -1, -1)))

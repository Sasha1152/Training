# https://py.checkio.org/uk/mission/write-quadratic-equation/


def get_sign(n):
    signs = {-1: '-', 1: '+', }
    if n == 0:
        return ''
    else:
        return f' {signs[n / abs(n)]} '


def quadr_equation(data: list[int]) -> str:
    """
    a*x**2 + b*x + c = 0
    x1 + x2 = -b / a
    x1 * x2 = c / a
    """
    if len(data) == 2:
        a, x1 = data
        x2 = x1
    else:
        a, x1, x2 = data

    c = int(x1 * x2 * a)
    b = int((-x1 - x2) * a)

    if a == 1:
        str_a = ''
    elif a == -1:
        str_a = '-'
    else:
        str_a = str(a) + '*'

    if b == 0:
        str_b = ''
    elif abs(b) == 1:
        str_b = f'x'
    else:
        str_b = f'{abs(b)}*x'

    return f'{str_a}x**2{get_sign(b)}{str_b}{get_sign(c)}{"" if c == 0 else abs(c)} = 0'


print(quadr_equation([2, 4, 6]))  # "2*x**2 - 20*x + 48 = 0"
print(quadr_equation([-2, 4, 6]))  # "-2*x**2 + 20*x - 48 = 0"
print(quadr_equation([2, 4, -4]))  # "2*x**2 - 32 = 0"
print(quadr_equation([2, 4, 0]))  # "2*x**2 - 8*x = 0"
print(quadr_equation([2, 0]))  # "2*x**2 = 0"
print(quadr_equation([2, 4]))  # "2*x**2 - 16*x + 32 = 0"
print(quadr_equation([1, 0]))  # 'x**2 = 0'
print(quadr_equation([-1, 0]))  # '-x**2 = 0'
print(quadr_equation([1, 1, 0]))  # 'x**2 - x = 0'

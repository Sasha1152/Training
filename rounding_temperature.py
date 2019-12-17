import math


def temp_round(num):
    if math.modf(abs(num))[0] >= 0.5:
        res = math.ceil(abs(num))
        return int(math.copysign(res, num))
    else:
        res = math.floor(abs(num))
        return int(math.copysign(res, num))


print(temp_round(9.8))
print(temp_round(9.2))
print(temp_round(-9.8))
print(temp_round(-9.2))

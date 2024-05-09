# https://py.checkio.org/uk/mission/leap-year-checking/


def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


# def is_leap_year(year: int) -> bool:
#     if year % 4 != 0:
#         return False
#     if year % 100 != 0:
#         return True
#     if year % 400 != 0:
#         return False
#     return True


print(is_leap_year(1500))

assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False

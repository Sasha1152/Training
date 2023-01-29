# https://py.checkio.org/uk/mission/is-string-a-number/

def is_number(val: str) -> bool:
    return val.isdigit()


print(is_number("123"))
print(is_number("123a"))
print(is_number(""))
print(is_number("abc"))
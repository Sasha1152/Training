# https://py.checkio.org/uk/mission/is-string-a-number-part-ii/

import re


def is_number(val: str) -> bool:
    return bool(re.match(r"^[+-]?(\d+\.?\d*|\.\d+)$", val))


assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1AAA") == False
assert is_number("1.") == True
assert is_number("+.l") == False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False
assert is_number('+.123') == True
assert is_number('.1') == True
assert is_number('.') == False

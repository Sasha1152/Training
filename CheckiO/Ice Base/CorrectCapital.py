# https://py.checkio.org/uk/mission/correct-capital/

import re


def correct_capital(line):
    return bool(re.match('^[a-zA-Z][a-z]*$|^[A-Z]*$', line))


print(correct_capital("CHECKIO"))

assert correct_capital("Checkio") == True
assert correct_capital("checkio") == True
assert correct_capital("CHECKIO") == True
assert correct_capital("CheCkio") == False

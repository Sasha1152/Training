# https://py.checkio.org/ru/mission/house-password/
import re

def checkio(data: str) -> bool:
    pattern = r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$'
    password = re.compile(pattern)
    if type(data) is not str:
        return False

    if not re.match(password, data):
        return False

    return True


assert checkio('A1213pokl') == False, "1st example"
assert checkio('bAse730onE4') == True, "2nd example"
assert checkio('asasasasasasasaas') == False, "3rd example"
assert checkio('QWERTYqwerty') == False, "4th example"
assert checkio('123456123456') == False, "5th example"
assert checkio('QwErTy911poqqqq') == True, "6th example"

print(checkio('bAse730onE4'))

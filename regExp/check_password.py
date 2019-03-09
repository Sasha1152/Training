import re


def check_pass(data: str) -> bool:

    password = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')

    if not data.match(password):
        return False

    return True


# if __name__ == '__main__':
#     assert check_pass('A1213pokl') == False, "1st example"
#     assert check_pass('bAse730onE4') == True, "2nd example"
#     assert check_pass('asasasasasasasaas') == False, "3rd example"
#     assert check_pass('QWERTYqwerty') == False, "4th example"
#     assert check_pass('123456123456') == False, "5th example"
#     assert check_pass('QwErTy911poqqqq') == True, "6th example"

print(check_pass('A1213pokl'))

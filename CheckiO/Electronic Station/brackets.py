# https://py.checkio.org/mission/brackets/solve/


def checkio(expression):
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    opening_br = '({['
    closing_br = ')]}'
    brackets_list = []

    for symb in expression:
        if symb in opening_br:
            brackets_list.append(symb)
        elif symb in closing_br:
            if not brackets_list:
                return False
            elif brackets_dict[symb] == brackets_list[-1]:
                brackets_list.pop()
            else:
                return False

    return not bool(brackets_list)


print(checkio("(])"))


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"



def checkio(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == s0:
            return False
    return True
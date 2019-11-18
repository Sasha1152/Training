# https://py.checkio.org/ru/mission/stressful-subject/

import re

def is_stressful(subj):
    if subj.isupper() or subj.endswith('!!!'):
        return True

    patterns = [
        r'h+\W?e+\W?l+\W?p+\W?',
        r'a+\W?s+\W?a+\W?p+\W?',
        r'u+\W?r+\W?g+\W?e+\W?n+\W?t+\W?'
    ]

    for pattern in patterns:
        if re.search(pattern, subj, re.IGNORECASE):
            return True

    return False


assert is_stressful("H.--i") is False
assert is_stressful("I neeed HELP") is True
assert is_stressful("H-E-L-P") is True
assert is_stressful("I neeed !!!") is True
assert is_stressful("AJDA..HHWF.UHFUG") is True
assert is_stressful('We need you A.S.A.P.!!') is True
assert is_stressful('UUUURGGGEEEEENT here') is True

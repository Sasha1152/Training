import re

def is_stressful(subj):
    if subj.isupper():
        return True
    elif subj[-3:] == '!!!':
        return True

    only_letters = ''

    for letter in subj:
        if letter.isalpha():
            only_letters += letter

    only_lower_letters = only_letters.lower()
    print(only_lower_letters)

    # stressful_words = ["help", "asap", "urgent"]
    patterns = [
        r'h+\W?e+\W?l+\W?p+\W?',
        r'a+\W?s+\W?a+\W?p+\W?',
        r'u+\W?r+\W?g+\W?e+\W?n+\W?t+\W?'
    ]
    for word in patterns:
        if word in only_lower_letters:
            return True

    return False


# assert is_stressful("H.--i") is False
# assert is_stressful("I neeed HELP") is True
# assert is_stressful("H-E-L-P") is TrueWe ne//ed you A.S.A.P.!!
# assert is_stressful("I neeed !!!") is True
# assert is_stressful("AJDA..HoHWF.UHFUG") is True
# assert is_stressful('We need you A.S.A.P.!!') is True
print(is_stressful('UUUURGGGEEEEENT here'))
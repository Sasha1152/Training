# https://py.checkio.org/ru/mission/roman-numerals/

def checkio(n):
    """
    I	1 (unus)
    V	5 (quinque)
    X	10 (decem)
    L	50 (quinquaginta)
    C	100 (centum)
    D	500 (quingenti)
    M	1000 (mille)
    """
    # rom_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arab_numbers = {1000: 'M',
                    900: 'CM',
                    500: 'D',
                    400: 'CD',
                    100: 'C',
                    90: 'XC',
                    50: 'L',
                    40: 'XL',
                    10: 'X',
                    9: 'IX',
                    5: 'V',
                    4: 'IV',
                    1: 'I'}
    rom_number = ''

    for key in arab_numbers:
        main, remainder = divmod(n, key)
        if remainder == n:
            continue
        else:
            rom_number += arab_numbers[key] * main
            n = remainder

    return rom_number


print(checkio(9))
print(checkio(76))  # 'LXXVI'
print(checkio(499))  # 'CDXCIX'
print(checkio(3888))  # 'MMMDCCCLXXXVIII'

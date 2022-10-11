# https://py.checkio.org/ru/mission/cipher-map2/

def recall_password(cipher_grille, ciphered_password):

    password = ''
    x_places = []
    cipher_grille = [list(s) for s in cipher_grille]
    for n in range(4):
        # print(cipher_grille)

        for i in range(4):
            for j in range(4):
                if cipher_grille[i][j] == 'X':
                    x_places.append((i, j))
                    password += ciphered_password[i][j]

        # print(x_places)
        cipher_grille = [['.' for i in range(4)] for j in range(4)]
        for x in x_places:
            cipher_grille[x[1]][abs(x[0] - 3)] = 'X'

        x_places = []

    return password


print(recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')))

assert recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd', 'First example'

assert recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

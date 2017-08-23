cipher_grille = ['X...','..X.','X..X','....']
ciphered_password = ["itdf","gdce","aton","qrdi"]
sentence = []
#print(ciphered_password[1][3])
for line in cipher_grille:
    for i in range(4):
        if i == 'X':
            sentence.append(ciphered_password[line][i])
print(sentence)

alphabet = ' abcdefghijklmnopqrstuvwxyz'  # length = 27

def ord(text, step):
    text_cipher = ''
    for letter in text:
        ind_alph = alphabet.index(letter)
        if (ind_alph + step) > len(alphabet) - 1:
            text_cipher += alphabet[ind_alph + step - len(alphabet)]
        else:
            text_cipher += alphabet[ind_alph + step]
    print(text_cipher)

def chr(text_cipher, step):
    text = ''
    for letter in text_cipher:
        ind_alph = alphabet.index(letter)
        if (ind_alph - step) > len(alphabet) - 1:
            text += alphabet[ind_alph - step + len(alphabet)]
        else:
            text += alphabet[ind_alph - step]
    print(text)


ord('need for speed', 10)
chr('xoonjpyajbzoon', 10)
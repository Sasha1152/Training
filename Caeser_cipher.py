alphabet = ' abcdefghijklmnopqrstuvwxyz' # lenght = 27

def ord(text, step):
    alphabet_cipher = ''
    text_cipher = ''
    for i in range(len(alphabet)):
        if (i + step) > len(alphabet) - 1:
            alphabet_cipher += alphabet[i + step - len(alphabet)]
        else:
            alphabet_cipher += alphabet[i + step]
    print(alphabet_cipher)

ord('abc', 20)
# https://py.checkio.org/uk/mission/morse-decoder/

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'}


def morse_decoder(code):
    morse_list = [a.split() for a in code.split('   ')]
    # print(morse_list)
    text_list = [''.join(list(map(lambda x: MORSE[x], l))) for l in morse_list]
    text = ' '. join(text_list).capitalize()
    # text = ''.join(list(map(lambda x: MORSE[x] if x else ' ', code.split(' ')))).capitalize()
    return text


print(morse_decoder("... --- -- .   - . -..- -"))  # "Some text"
print(morse_decoder("..--- ----- .---- ---.."))  # "2018"
print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))  # "It was a good day"

print("... --- -- .   - . -..- -".replace('   ',' # ').split())

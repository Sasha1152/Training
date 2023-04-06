# https://py.checkio.org/uk/mission/morse-encoder/

MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " "
}


def morse_encoder(text: str) -> str:
    text_list = list(text.lower())
    morse_list = list(map(lambda x: MORSE[x], text_list))
    return ' '.join(morse_list)

# def morse_encoder(text: str) -> str:
#     return ' '.join(MORSE[i] for i in text.lower())


print(morse_encoder("Some Text"))

assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")


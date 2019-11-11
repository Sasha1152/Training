# https://py.checkio.org/ru/mission/bird-language/

VOWELS = "aeiouy"

def translate(phrase):
    true_phrase = ''
    i = 0
    while i < len(phrase):
        true_phrase += phrase[i]
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    return true_phrase

print(translate('hieeelalaooo'))
print(translate('hoooowe yyyooouuu'))
print(translate('hoooowe yyyooouuu duoooiiine'))


assert translate("hieeelalaooo") == "hello", "Hi!"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

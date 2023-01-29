# https://py.checkio.org/uk/mission/backward-each-word/

def backward_string_by_word(text: str) -> str:
    text_list = text.split(' ')
    for i in range(len(text_list)):
        text_list[i] = text_list[i][::-1]
    rewersed_text = ' '.join(text_list)

    return rewersed_text


print(backward_string_by_word(''))
print(backward_string_by_word('world'))
print(backward_string_by_word('hello world'))
print(backward_string_by_word('hello   world'))
print(backward_string_by_word('welcome to a game'))


def backward_string_by_word(text: str) -> str:
    return " ".join(map(lambda x: x[::-1], text.split(' ')))


def backward_string_by_word2(text: str) -> str:
   return ' '.join(reversed(text[::-1].split(' ')))


def backward_string_by_word3(text: str) -> str:
    return ' '.join([word[::-1] for word in text.split(' ')])

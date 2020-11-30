def backward_string_by_word(text: str) -> str:
    rewersed_text = ''
    rewersed_word = ''
    for letter in text:
        if letter:
            rewersed_word = letter + rewersed_word
        else:
            rewersed_word = ''
        rewersed_text += rewersed_word
    return rewersed_text



print(backward_string_by_word(''))
print(backward_string_by_word('world'))
print(backward_string_by_word('hello world'))
print(backward_string_by_word('hello   world'))
print(backward_string_by_word('welcome to a game'))

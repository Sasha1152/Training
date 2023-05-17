# https://py.checkio.org/uk/mission/monkey-typing/

def count_words(text: str, words: set) -> int:
    counter = 0
    for word in words:
        counter += bool(text.lower().count(word))
    return counter


print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", {"sum", "hamlet", "infinity", "anything"}))

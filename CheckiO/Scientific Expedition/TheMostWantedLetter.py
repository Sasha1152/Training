# https://py.checkio.org/uk/mission/most-wanted-letter/

def checkio(text: str) -> str:
    letters_counter = {}
    text = text.lower()

    for letter in text:
        if letter.isalpha():
            if letter in letters_counter:
                letters_counter[letter] += 1
            else:
                letters_counter[letter] = 1
        else:
            continue

    max_number = max(letters_counter.values())
    for letter, count in sorted(letters_counter.items()):
        if count < max_number:
            del letters_counter[letter]
    most_common_letter = sorted(letters_counter)[0]

    return most_common_letter


print(checkio('How do you do?'))

assert checkio("Hello World!") == "l", "Hello test"
assert checkio("How do you do?") == "o", "O is most wanted"
assert checkio("One") == "e", "All letter only once."
assert checkio("Oops!") == "o", "Don't forget about lower case."
assert checkio("AAaooo!!!!") == "a", "Only letters."
assert checkio("abe") == "a", "The First."
assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."


def checkio(text):
    l = [a for a in text.lower() if a.isalpha()]
    return  max(sorted(l), key=l.count)
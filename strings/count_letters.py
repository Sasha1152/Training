text = 'ThiS is String with Upper and lower case Letters'
def letter_count(a):
    a = a.lower()
    a = a.replace(' ', '')
    # print(a)
    counter_letters = {}
    for letter in a:
        if letter in counter_letters:
            counter_letters[letter] += 1
        else:
            counter_letters[letter] = 1
    # print(counter_letters)
    for key, value in sorted(counter_letters.items()):
        # print(key + ':', value) ???????????????
        print(key + ': '),
        print(value)

letter_count(text)

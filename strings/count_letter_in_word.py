def count_letter(word, letter):
    n = 0
    for i in word:
        if i == letter:
            n = n + 1
    return n

print(count_letter('banana', 'a'))
def is_palindrome(word):
    reversed_word = ''
    for letter in word:
        reversed_word = letter + reversed_word
        print(reversed_word)
    return reversed_word == word

assert is_palindrome('ABBA') == True
assert is_palindrome('OKKO') == True
assert is_palindrome('bulbs') == False


def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(int(len(s) / 2)))

assert is_palindromic('ABBA') == True
assert is_palindromic('OKKO') == True
assert is_palindromic('bulbs') == False
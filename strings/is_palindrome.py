def is_palindrome(s):
    reverse_word = ''
    for letter in s:
        reverse_word = letter + reverse_word
        # print(rewerse_word)
    return reverse_word == s

assert is_palindrome('ABBA') == True
assert is_palindrome('OKKO') == True
assert is_palindrome('bulbs') == False


def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(int(len(s) / 2)))

assert is_palindromic('ABBA') == True
assert is_palindromic('OKKO') == True
assert is_palindromic('bulbs') == False
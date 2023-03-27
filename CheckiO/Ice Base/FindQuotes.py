# https://py.checkio.org/en/mission/find-quotes/

import re


def find_quotes(a):
    words_in_quates = re.findall(r'"[^"]*"', a)
    words = list(map(lambda x: x.strip('"'), words_in_quates))
    return words


print(find_quotes('"Greetings"'))
print(find_quotes('"Greetings" testing words "DF" "word"'))
print(find_quotes('Рш'))
print(find_quotes('good morning mister "superman"'))
print(find_quotes('"this" doesn\'t make any "sense"'))
print(find_quotes('"Lorem Ipsum" is simply dummy text '))

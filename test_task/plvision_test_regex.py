# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

import re


def is_good_string(string):
    """
        >>> is_good_string('()')
        True
        >>> is_good_string('()[]{}')
        True
        >>> is_good_string('(]')
        False
        >>> is_good_string('([)]')
        False
        >>> is_good_string('{[]}')
        True
        >>> is_good_string('[{([])}{{(([]))}}]')
        True
        >>> is_good_string('[{([])}{{(([]))}}[]')
        False
        >>> is_good_string('')
        True
    """

    pattern = r'\(\)|\[\]|\{\}'
    while re.search(pattern, string):
        string = re.sub(pattern, '', string)

    return not string



if __name__ == '__main__.py':
    import doctest
    doctest.testmod()

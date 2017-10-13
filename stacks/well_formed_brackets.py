from Algorithm import Algorithm
from stacks.Stack import Stack


def well_formed_brackets(s):
    lookup = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    left_chars = Stack()

    for i in range(0, len(s)):
        if s[i] in lookup.keys():
            left_chars.push(s[i])
        elif left_chars.is_empty() or s[i] != lookup[left_chars.pop()]:
            return False

    return left_chars.is_empty()


class WellFormedBrackets(Algorithm):
    pass
from stacks.Stack import Stack


def well_formed_brackets(s):
    """
    A string of brackets is well-formed if they are closed in the correct order
    i.e. [{()}] is well formed, but [}](){ is not.
    :param s: string
    :return: boolean
    """
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


import string


def column_to_int(s):
    sum = 0
    for i, c in enumerate(reversed(s)):
        sum += (string.ascii_uppercase.index(c) + 1) * (26 ** i)

    return sum

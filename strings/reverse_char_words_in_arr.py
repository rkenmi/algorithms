"""
    This is similar to `reverse_words_in_str.py` except that the array consists of
    chars only.

    i.e. ['A', ' ', 'K', 'a', 'p', 'p', 'a', ' ', 'p', 'u', 'n', 'c', 'h']

    should return

    ['p', 'u', 'n', 'c', 'h', ' ', 'K', 'a', 'p', 'p', 'a', ' ', 'A']
"""

def reverse_words(arr):
    list.reverse(arr)
    start, end = 0, len(arr) - 1

    for i in range(len(arr) + 1):  # if there is no space, we still need to reverse it (because the chars are flipped)
        if i == len(arr) or arr[i] == ' ':
            end = i - 1  # we want to skip swapping spaces! they're fine where they are
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            start = i + 1  # we don't want start to point to i, since i == ' '

    return arr
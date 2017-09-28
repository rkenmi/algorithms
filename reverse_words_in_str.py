# assume s is a bytearray, return a string with reversed words

def reverse_in_range(s, start, end, lazyass=False):
    if lazyass:
        s[start:end] = bytearray(reversed(s[start:end]))
    else:
        end -= 1
        while start < end:  # this is O(k) for k < n and k is a small subarray in n that hasn't been visited
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

def reverse_words(s):
    s = bytearray(reversed(s))

    front = 0
    while front < len(s):  # this is O(n) since all elements are visited once
        end = s.find(b' ', front)
        if end is -1:
            break
        reverse_in_range(s, front, end)
        front = end+1

    reverse_in_range(s, front, len(s))
    return s.decode()


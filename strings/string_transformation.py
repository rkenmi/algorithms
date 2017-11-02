"""
String s is an array of lowercase English characters (a-z) index from 0 to N - 1.
Each index i (where 0 <= i < N) in s contains character s_i.

Iterate through each character in s and, for each index i, count the occurrences, k, of s_i in the inclusive
range of indices from 0 to i-1. Then cyclically increment character s_i by k and save the resulting value
to index i in a new string, q.

Given s, find string q and print it on a new line.

Note: Cyclically incrementing a lowercase character by an integer means that a + 1 = b, b + 2 = d, and z + 1 = a

"""

def transform_string(s):
    s_arr = list(s)
    d = {}

    result = []

    for i in range(len(s_arr)):
        if s_arr[i] in d:
            d[s_arr[i]] += 1
            if d[s_arr[i]] == 27:
                d[s_arr[i]] = 1
        else:
            d[s_arr[i]] = 1

        unicode_int_code = ord(s_arr[i]) + (d[s_arr[i]] - 1)
        if unicode_int_code - ord('a') > 25:
            unicode_int_code -= (ord('z') - ord('a') + 1)

        result.append(chr(unicode_int_code))

    return "".join(result)

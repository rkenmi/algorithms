"""
    Given an array of fixed length strings (where n = fixed length),
    Sort the strings in ascending order.

    (Use LSD String Radix Sort)
"""
def fixed_length_strings(A, n):
    R = 255  # assume that there are 255 distinct characters ASCII style
    i = n-1

    result = ["$" for _ in range(len(A))]  # the $ will get replaced, so it doesn't hold any meaning

    #  Do Key Index Counting

    for k in range(n-1, -1, -1):  # sweep right to left, since left has greatest precedence in sorting strings
        count = [0] * (R+1)

        # First stage: count the frequencies of each character
        for s in A:
            char_int = ord(s[k]) + 1  # reserve index 0
            count[char_int] += 1

        # Second stage: accumulate sum
        running_sum = 0
        for i in range(len(count)):
            running_sum += count[i]
            count[i] = running_sum

        # Third stage: Use count to map new placement of value based on k'th character in the group of strings.
        for i in range(len(A)):
            char_int = ord(A[i][k])
            result[count[char_int]] = A[i]  # just copy the appropriate string based on k'th characters order
            count[char_int] += 1

    return result

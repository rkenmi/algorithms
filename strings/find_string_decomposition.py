def get_str_decomp(s, keywords):
    from collections import Counter
    counter = Counter(keywords)
    keys_remaining = len(keywords)
    l = len(keywords[0])

    def _get_decomp(i, remaining):
        if remaining == 0:
            return i
        elif i >= len(s):
            return -1

        word = s[i:i+l]

        if word in counter and counter[word] > 0:
            counter[word] -= 1
            is_part_of_concat = _get_decomp(i+l, remaining - 1)
            counter[word] += 1

            if is_part_of_concat > -1:
                return i

        result = _get_decomp(i+1, remaining)
        return result

    return _get_decomp(0, keys_remaining)


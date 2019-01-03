def find_smallest_substring_covering_set(text, keywords):
    from collections import Counter

    keyword_counter = Counter(keywords)
    remaining_keywords = len(keywords)
    left = 0
    result = (-1, -1)

    for right, right_word in text:
        if right_word in keywords:
            keyword_counter[right_word] -= 1

            if keyword_counter[right_word] == 0:
                remaining_keywords -= 1

        while remaining_keywords == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)

            left_word = text[left]
            if left_word in keywords:
                keyword_counter[left_word] += 1
                remaining_keywords += 1

            left += 1

    return result 
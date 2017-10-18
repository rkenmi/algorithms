"""
    Given a list of integers and an integer k, return a list of pairs (x, y) where x - y is equal to k.
"""
import bisect


def exact_difference(A, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    :param A:
    :param k:
    :return:
    """
    record = {}
    for num in A:
        record[num] = True

    pairs = []
    for num in A:
        if record.get(num - k) is not None:
            pairs.append([num, num - k])

    return pairs


def exact_difference_no_space(A, k):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(1)  ; additional, that is
    :param A:
    :param k:
    :return:
    """
    list.sort(A)
    pair_counter = 0
    for i, num in enumerate(A):
        match = bisect.bisect_left(A, num-k, lo=pair_counter)
        if match != len(A) and A[match] is num-k:
            A[pair_counter] = [num, num-k]
            pair_counter += 1

    return A[:pair_counter]

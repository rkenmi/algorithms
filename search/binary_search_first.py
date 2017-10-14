import bisect

from Algorithm import Algorithm


def binary_search_first_naive(A, target):
    index_of_target = bisect.bisect_left(A, target)

    if not (0 <= index_of_target < len(A)):
        return -1  # bisect_left returns different index if it fails, so catch it and return expected index

    first_occurence = -1
    for i in range(index_of_target, -1, -1):  # reverse iterate
        if A[i] is A[index_of_target]:
            first_occurence = i

    return first_occurence


def binary_search_first(A, target):
    """
    Searches A for the *first* occurrence of target in the sorted array and returns that index.
    -1 if not found.
    :param A:
    :param lo:
    :param hi:
    :param target:
    :return:
    """
    def binary_search(A, lo, hi, target):
        if lo > hi:
            return -1

        # Beware, this can cause overflow
        mid = (lo + hi) // 2

        if A[mid] is target:
            left_subtree = binary_search(A, lo, mid-1, target)
            return left_subtree if left_subtree > -1 else mid
        elif A[mid] < target:
            return binary_search(A, mid+1, hi, target)
        elif A[mid] > target:
            return binary_search(A, lo, mid-1, target)

    return binary_search(A, 0, len(A)-1, target)

class BinarySearchFirst(Algorithm):
    pass
"""
    Grabbing the min and max of an unsorted array (of numbers)
    can cost about 2(n-1) compares.

    Simply:

    for n in array:
        min_n, max_n = min(n, min_n), max(n, max_n)

    Is there a way to reduce the number of compares?
"""


def min_max_less_compares(A):
    """
        (3n/2)-2 compares version, which is < 2(n-1) compares
    :param A:
    :return:
    """
    # 2 compares
    min_val = min(A[0], A[1])
    max_val = max(A[0], A[1])

    for i in range(2, len(A)-1, 2):
        # 1 compare
        local_min, local_max = (A[i], A[i+1]) if A[i] < A[i+1] else (A[i+1], A[i])

        # 2 compares
        min_val = min(local_min, min_val)
        max_val = max(local_max, max_val)

    return min_val, max_val





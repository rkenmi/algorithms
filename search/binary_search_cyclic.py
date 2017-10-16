def binary_search_cyclic(A):
    def _search(A, lo, hi):
        if lo > hi:
            return -1

        if lo is hi:
            return lo

        mid = (lo + hi) // 2
        if A[mid] > A[hi]:
            return _search(A, mid+1, hi)
        else:
            small = _search(A, lo, mid-1)
            return small if A[small] < A[mid] else mid

    return _search(A, 0, len(A)-1)


def binary_search_cyclic_iterative(A):
    left = 0
    right = len(A) - 1
    if not A:
        return -1

    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid+1
        else:
            right = mid-1
            if A[mid] < A[left]:
                left = mid

    return left
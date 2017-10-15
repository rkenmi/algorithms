def binary_search_cyclic(A):
    def _search(A, lo, hi):
        if lo is hi:
            return lo

        mid = lo + hi // 2
        if A[mid] > A[hi]:
            return _search(A, mid+1, hi)
        else:
            small = _search(A, lo, mid-1)
            return small if A[small] < A[mid] else mid

    return _search(A, 0, len(A)-1)


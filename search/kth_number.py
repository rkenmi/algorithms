"""
Given an array with *distinct* values (no duplicates), return the kth largest number.

[3, 9, 4, 1, 0]

pivot = 3

[1, 0, 3, 9, 4]

"""
def kth_largest(A, k, start=None, end=None):
    def _partition(A, pivot, start, end):
        lo = curr = start
        hi = end
        val = A[pivot]

        while curr <= hi:
            if A[curr] < val:
                A[lo], A[curr] = A[curr], A[lo]
                lo += 1
                curr += 1  # curr always stays ahead of lo
            elif A[curr] > val:
                A[hi], A[curr] = A[curr], A[hi]
                hi -= 1
            else:  # A[curr] == val
                curr += 1

        return curr - 1

    import random

    if not A:
        raise IndexError("List is empty")

    if k > len(A):
        raise ValueError("k cannot be a number greater than the List size")

    if not (start and end):
        start, end = 0, len(A)-1

    pivot = random.randint(start, end)
    pivot = _partition(A, pivot, start, end)
    n = len(A) - pivot
    if n is k:
        return A[pivot]
    elif k < n:  # we can skip the left subtree
        return kth_largest(A, k, start=pivot+1, end=end)
    else:  # k > n, we can skip the right subtree
        return kth_largest(A, k, start=start, end=pivot-1)





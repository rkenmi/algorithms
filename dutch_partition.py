def dutch_partition(A, i):
    """
    The strategy is to have 3 pointers: low, high, and curr

    low gets incremented when we know for sure that elements
    at index 0-low are indeed lower than the pivot value.

    hi gets decremented when we know for sure that elements
    at index hi-len(A) are indeed higher than the pivot value.

    curr serves as the iterating index. curr gets automatically incremented
    when we swap new values into index 0-low because curr also acts
    as the pointer for values *equivalent* to the pivot value.

    the reason for this is simple; curr should always be ahead of the
    low ptr because index 0-low are values that are strictly
    lower than the pivot value. so if we increment the low ptr,
    we also need to increment the curr ptr.

    when we swap values into hi-len(A), we only decrement the hi ptr.
    we do NOT change curr because the position of hi has no
    bearing with the position of curr or low.

    lastly, we increment curr in the case that we do come across
    values equivalent to the pivot value.

    all in all, this is a sweet and concise algorithm because it doesn't use
    a for loop and it takes advantage of the curr ptr being the iterator index
    for the while loop AND a ptr that keeps track of equivalent values

    naturally, we terminate the loop if curr <= hi.
    a small caveat; why curr <= hi instead of curr < hi?
    well, there is a possibility that hi is never decremented,
    which means only index 0-(len(A)-1) will go thru the partitioning,
    effectively skipping the last element.

    :param A: the list to partition
    :param i: the index of the pivot
    :return: None (A will be modified in-place)
    """
    pivot = A[i]
    low = curr = 0
    hi = len(A) - 1

    while curr <= hi:
        if A[curr] < pivot:
            A[low], A[curr] = A[curr], A[low]
            low += 1
            curr += 1
        elif A[curr] > pivot:
            A[hi], A[curr] = A[curr], A[hi]
            hi -= 1
        else: # A[curr] == pivot
            curr += 1


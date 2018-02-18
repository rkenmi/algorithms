import heapq

DECREASING = 0
INCREASING = 1


def sort_k_inc_dec(A):
    """
    Given an k-increasing-decreasing array, sort the array.
    
    For example, [1, 2, 6, 4, 2, 3] is a 3-increasing-decreasing array because it increases
    once from [1, 2], decreases from [6, 4], then increases again from [2, 3].

    :param A:
    :return:
    """
    if not A:
        return

    prev = A[0]
    begin = 0
    decreasing, increasing = [], []  # indices to start from
    mode = None
    for i in range(1, len(A)):
        val = A[i]
        if mode is None:
            mode = INCREASING if val >= prev else DECREASING
        else:
            if mode == INCREASING and prev > val:
                increasing.append([begin, i-1])
                begin = i
                mode = None
            elif mode == DECREASING and val >= prev:
                decreasing.append([begin, i-1])
                begin = i
                mode = None
        prev = val

    if mode is INCREASING:
        increasing.append([begin, len(A)-1])
    elif mode is DECREASING:
        decreasing.append([begin, len(A)-1])

    heap, result = [], []
    while heap or (increasing or decreasing):
        for i, subarray in enumerate(decreasing):
            begin, end = subarray
            if begin <= end:
                heapq.heappush(heap, A[end])
                decreasing[i][1] = end - 1
            else:
                decreasing.pop(i)

        for i, subarray in enumerate(increasing):
            begin, end = subarray
            if begin <= end:
                heapq.heappush(heap, A[begin])
                increasing[i][0] = begin + 1
            else:
                increasing.pop(i)

        if heap:
            result.append(heapq.heappop(heap))

    return result


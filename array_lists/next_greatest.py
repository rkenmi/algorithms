import math

from Algorithm import Algorithm

def next_greatest_naive(A):
    """
    Given an array, return a mapping of the next greatest element for each element
    i.e.

    [1, 5, -3, 9, -4, 7]


    1: 5
    5: 9
    -3: 9
    9: None
    -4: None

    :return: dictionary mapping
    """
    record = {}
    for i in range(len(A)):
        record[A[i]] = None
        for j in range(i, len(A)):
            if A[i] < A[j]:
                record[A[i]] = A[j]
                break

    return record



def next_greatest(A):
    """
    Given an array, return a mapping of the next greatest element for each element
    i.e.

    [1, 5, -3, 9, -4, 7]


    1: 5
    5: 9
    -3: 9
    9: None
    -4: None

    :return: dictionary mapping
    """
    record = {}
    stack = []
    curr_max = -math.inf
    for elem in A:
        if elem > curr_max:
            while stack:
                seen = stack[-1]
                if seen < elem:
                    stack.pop()
                    record[seen] = elem
                else:
                    break

        curr_max = elem
        record[elem] = None
        stack.append(elem)

    return record

class NextGreatest(Algorithm):
    pass


"""
    Given two sorted arrays, merge both of them INTO the first array.

    Assume the first array has enough space for both arrays.

"""


def merge_into_A1_naive(A1, A2):
    # Time: O(n log n)
    count = 0
    while A1[count] is not None:
        count += 1

    for x in A2:
        A1[count] = x
        count += 1

    list.sort(A1)
    return A1


def merge_into_A1_fast(A1, A2):
    """
        Take advantage of the empty space in A1

        Caveats:
            - Traverse backwards
            - Start writing from the endpoint, which is # of valid elements in A1 + A2
            - Overwrite elements as you move backwards. It is guaranteed that we don't need the elements you overwrite.

        Time: O(n)
        Space: O(1)
    :param A1:
    :param A2:
    :return:
    """
    count = 0
    while A1[count] is not None:
        count += 1

    endpoint = count + len(A2) - 1

    p1, p2 = count-1, len(A2)-1
    while p1 >= 0 and p2 >= 0 and endpoint >= 0:
        if A1[p1] > A2[p2]:
            A1[endpoint] = A1[p1]
            p1 -= 1
            endpoint -= 1
        else:
            A1[endpoint] = A2[p2]
            p2 -= 1
            endpoint -= 1

    remaining = max((p1, A1), (p2, A2))
    p, A = remaining
    while p >= 0 and endpoint >= 0:
        A1[endpoint] = A[p]
        p -= 1
        endpoint -= 1

    return A1


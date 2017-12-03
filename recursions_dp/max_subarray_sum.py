"""
    Find the maximum sum over all subarrays of a given array of integer.

    Example:
        [904, 40, 523, 12, -335, -385, -124, 481, -31]

    Output:
        1479
    (Add from index 0 to index 3)
"""

def max_subarray_brute(A):
    max_sum = 0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            sum = 0
            for k in range(i, j+1):
                sum += A[k]

            max_sum = max(sum, max_sum)

    return max_sum


def max_subarray_better(A):
    """
        Improves on the brute force method by pre-computing the sums into storage beforehand

        Example:
            [904, 40, 523, 12, -335, -385, -124, 481, -31]

        =>  [904, 944, 1467, 1479, 1144, 759, 635, 1116, 1185]
    :param A:
    :return:
    """
    sums = [0] * len(A)
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        sums[i] = sum

    max_sum = 0
    for j in range(0, len(A)):
        for k in range(j, len(A)):
            if j == k:
                max_sum = max(sums[j], max_sum)

            sum = sums[k] - sums[j]
            max_sum = max(sum, max_sum)

    return max_sum

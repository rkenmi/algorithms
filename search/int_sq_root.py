def int_square_root(n):
    """
    Given an integer n, find the integer square root.
    i.e. int_square_root(64) => 8, int_square_root(69) => 8, int_square_root(81) => 9
    :param n: positive Integer
    :return: Integer square root
    """
    # left represents minimum interval, right represents max interval. Similar to binary search.
    left, right = 0, n

    while left < right:
        mid = (left + right) // 2
        if mid ** 2 < n:
            left = mid + 1

            # If our new left's square exceeds n, that means we're done with our search; we found our int square root
            # Since right is always > than left, if left's square > n then right's square > n.
            if left ** 2 > n:
                return mid
        elif mid ** 2 == n:
            return mid
        else:  # mid ** 2 > n
            right = mid - 1

    return left




def get_min_from_rotated_sorted_array(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] < A[right]:
            # rotation must be in left subarray
            right = mid
        else:
            left = mid + 1

    return left

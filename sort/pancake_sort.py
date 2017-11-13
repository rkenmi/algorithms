"""
    Implement a sort using flipped (reversed) data.

    1. Create a flip function that reverses an array up to the kth element
    2. Sort the original array while utilizing the flip function

"""

def pancake_sort(arr):
    import math

    def flip(arr, k):
        i = 0
        k -= 1
        while i < k:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k -= 1

    def max_index_in_subarray(arr, n):
        i = 0
        greatest = -math.inf
        max_index = -1
        while i < n:
            if arr[i] > greatest:
                max_index = i
                greatest = arr[i]
            i += 1

        return max_index

    size = len(arr)
    while size > 0:
        max_index = max_index_in_subarray(arr, size)
        flip(arr, max_index + 1)
        flip(arr, size)

        size -= 1
    return arr


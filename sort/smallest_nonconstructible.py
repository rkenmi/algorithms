"""
    Given an array with random integers, find the smallest non-constructible integer in the array.

    Ex:
    [1, 3, 5] => 2
    We can make 1 using 1 in the array. We can make 3 using 3 in the array.
    We can make 4 using 1 and 3 in the array. We can make 5 using 5 in the array.
    We can't make 2 no matter what combination of ints we use.
    2 is also the lowest number we can't make.
    We can't make 7 either, but 2 < 7 so the fcn returns 2.


    [1, 2, 3, 5] => 12
    12 cannot be made since 1 + 2 + 3 + 5 is 11, and that's the highest sum possible

    1 2 4:  1 2 3 4 5 6
    1 2 5:  1 2 3 5 6 7
    1 2 6:  1 2 3 6 7 8
    1 3 6:  1 3 4 6 7 9 10
    1 3 7:  1 3 4 7 8 10 11
    1 3 8:  1 3 4 8 9 11 12
"""

def smallest_nonconstructible(A):
    list.sort(A)
    running_sum = A[0]

    for num in A[1:]:
        if running_sum != num - 1:
            return running_sum + 1
        running_sum += num

    return running_sum

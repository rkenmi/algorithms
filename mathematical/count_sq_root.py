"""
Given two integer intervals begin and end,

Return the count of all perfect squares in the interval.

"""

# def count_sq_root_slow(begin, end):
#     from math import sqrt
#     if begin < 2:
#         begin = 2
#
#     count = 0
#     for i in range(begin, end+1):
#         if i == 1:
#             continue
#
#         if sqrt(i) - int(sqrt(i)) == 0:
#             count += 1
#
#     return count
#
#
# def count_sq_root_better(begin, end):
#     from math import sqrt
#     if begin < 2:
#         begin = 2
#
#     count = 0
#     for i in range(int(sqrt(begin)), int(sqrt(end))+1):
#         if i == 1:
#             continue
#
#         if sqrt(i ** 2) - int(sqrt(i ** 2)) == 0:
#             count += 1
#
#     return count


def count_sq_root_slow(begin, end):
    """
        Suppose begin = 3, end = 10
        We know that perf. squares between 3 and 10 are 4 (2*2) and 9 (3*3).

        Perfect squares have the following formula: SUM_FROM_k=1_to_n (2k - 1), where N is the square root number.
        For example, if n = 2 then:
            (2(1) - 1) + (2(2) - 1) =  1 + 3 = 4
                where 4 is just 2 squared.

        if n = 3 then:
            (2(1) - 1) + (2(2) - 1) + (2(3) - 1) = 1 + 3 + 5 = 9
                where 9 is just 3 squared

    :param begin:
    :param end:
    :return:
    """

    def is_perfect_square(x):
        count = 0
        next_odd = 1
        while count < x:
            count += next_odd
            next_odd += 2

        return count == x

    count_perf_sq = 0
    for i in range(begin, end):
        if is_perfect_square(i):
            count_perf_sq += 1

    return count_perf_sq



def count_sq_root_fast(begin, end):
    """
        Although the formula above is interesting, there is a much, much faster way to get the perfect squares
        in an interval.

        Simple Explanation:
            If you have <4, 64>, try taking a sq root of both ends.
            You will get <2, 8>. But notice that, each number between 2 and 8 can be squared
            and that number will be in <4, 64>.
            2**2 = 4 is in <4, 64>
            3**2 = 9 is in <4, 64>
            4**2 = 16 is in <4, 64>
            5**2 = 25 is in <4, 64>
            ...
            8**2 = 64 is in <4, 64>

        Extended Explanation (Edge cases):
            Suppose begin = 3, end = 24
            We know that perf. squares between 5 and 24 are 9 (3*3), and 16 (4*4).

            If we take the square root of 5, we will get ~~2.2, which will be 2 if rounded.
                and if we take the square root of 24, we will get ~~4.9, which will be 5 if rounded.

            We notice that the rounded 2, when squared, is not relevant to our interval.
            2^2 = 4, which is a perfect square, but it is outside of the interval <5, 24>.

            The round operation is including extra perfect squares now.
            We only care about the perfect squares AFTER 5.
            So, when we get the square root of 5
            and get ~~2.2, it doesn't make sense to *decrease* it because we know that a number < (2.2)^2
            will always be less than the minimum of our interval (which is 5).
            Instead of rounding down, we should use the Ceiling operation to get the next
            Integer (which would be 3), since we'll know for sure that 3^2 will be in the <5, 24> interval after
            squaring.

            Let's look at the rounded 5 now. 5^2 = 25, and again that is outside of the interval <5, 24>.
            Using the same kind of logic above, it doesn't make sense to increase our ~~4.9 to any higher value, let alone
            5.
            Here, since we want smaller values, we will floor the square root of the end interval.
            This means floor(~~4.9) = 4.

            So now we have our new rounded numbers after the floor/ceil operations: 3 and 4.
            And indeed, all numbers between 3 and 4 inclusive, when squared, are inside the interval <5, 24>.
            All we need to do is count the squares between 3 and 4.
            This is as simple as 4 - 3, but we need to remind ourselves that we want to count inclusively, so we add
            a 1 to that difference.

            floor(end) - ceil(begin) + 1 = # of perf. squares

    :param begin:
    :param end:
    :return:
    """
    import math

    #  return result is guaranteed to be int
    return math.floor(math.sqrt(end)) - math.ceil(math.sqrt(begin)) + 1

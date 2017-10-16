import math

"""
    This is a classic array problem.
    
    We buy a stock (integer) at some index in A and sell the stock at some later index in A.
    We want to find the maximum profit we can get from buying and selling the stock at various times in A.
    
    The key to solving this is that we want to buy a stock and intuitively speaking, if we're gonna
    buy a stock, we want to buy the *smallest* or cheapest stock there is because that has the possibility of
    biggest profit. So, we want to always be alert when we come across the smallest number we've seen as we
    traverse A. 
    
    1. If we come across the smallest number we've seen thus far, then we'll choose to buy that stock
    and see how it goes.
    
    Now, if we come across numbers that aren't the smallest we've seen yet, then we'll want to compute the difference
    because that will net us the profit. But, we don't really care about recording profit if its less than what
    we have already recorded.
    
    2. When we compute the profits, just store the maximum of the new profit or the profit we have currently.
    
    For examples, refer to array_lists.tests.py
    
"""

def buy_and_sell_stock_naive(A):
    if not A:
        return 0

    profits = 0

    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[j] > A[i]:
                profits = max(profits, A[j] - A[i])

    return profits


def buy_and_sell_stock_forward(A):
    """
    Strategy 1: Iterate in regular order and store the difference of the smaller values.
    If current value is smaller, then reset; That value will be the new number to subtract.

    Time: O(n)
    Space: O(1)
    :param A:
    :return:
    """
    if not A:
        return 0

    start_sell = A[0]
    max_profit = 0

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            max_profit = max(max_profit, A[i] - start_sell)
        else:
            start_sell = A[i]

    return max_profit


def buy_and_sell_stock_reverse(A):
    """
    Strategy 1b: Iterate in reverse order and store the difference of the smaller values.
    If current value is larger, then reset; That value will be the new number to take future differences from.

    Time: O(n)
    Space: O(1)
    :param A:
    :return:
    """
    if not A:
        return 0

    take_diff_from = A[-1]
    max_profit = 0

    for i in range(len(A)-2, -1, -1):
        if A[i] < A[i+1]:
            max_profit = max(max_profit, take_diff_from - A[i])
        else:
            take_diff_from = A[i]

    return max_profit

def buy_and_sell_stock_clean(A):
    min_price, max_profit = math.inf, 0

    for num in A:
        max_profit = max(num - min_price, max_profit)
        min_price = min(num, min_price)

    return max_profit





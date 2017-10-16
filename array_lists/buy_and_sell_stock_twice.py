import math


def buy_and_sell_stock_twice_naive(A):
    if not A:
        return 0

    min_1st_price, max_1st_profit = math.inf, 0
    max_overall_profit = 0
    for i in range(0, len(A)):
        max_1st_profit = max(A[i] - min_1st_price, max_1st_profit)
        min_1st_price = min(A[i], min_1st_price)

        min_2nd_price, max_2nd_profit = math.inf, 0
        for j in range(i + 1, len(A)):
            max_2nd_profit = max(A[j] - min_2nd_price, max_2nd_profit)
            min_2nd_price = min(A[j], min_2nd_price)

        max_overall_profit = max(max_1st_profit + max_2nd_profit, max_overall_profit)

    return max_overall_profit


def buy_and_sell_stock_twice(A):
    profits = [0] * len(A)
    min_price = math.inf

    for i, num in enumerate(A):
        profits[i] = num - min_price
        min_price = min(num, min_price)

    max_profit_1, max_profit_2 = 0, 0
    for stock in reversed(profits):
        if stock > max_profit_1:
            max_profit_2 = max_profit_1
            max_profit_1 = stock
        elif stock > max_profit_2:
            max_profit_2 = stock

    return max_profit_1 + max_profit_2

def buy_and_sell_stock_twice(A):
    profit = 0
    min_so_far = A[0]

    running_profit_fwd = []
    running_profit_bwd = []

    for num in A:
        if num < min_so_far:
            min_so_far = num
        profit = max(profit, num - min_so_far)
        running_profit_fwd.append(profit)

    max_so_far = A[-1]
    profit = 0
    for num in reversed(A):
        if num >= max_so_far:
            max_so_far = num
        profit = max(profit, max_so_far - num)
        running_profit_bwd.append(profit)

    running_profit_bwd = running_profit_bwd[::-1]

    total_profits = []
    for i, num in enumerate(running_profit_bwd):
        if i == 0:
            total_profits.append(running_profit_bwd[i])
        else:
            total_profits.append(running_profit_bwd[i] + running_profit_fwd[i-1])

    return max(total_profits)



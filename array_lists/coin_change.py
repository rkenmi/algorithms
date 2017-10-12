
def coin_change_dynamic(coins, amount):

    amount_arr = [-1] * (amount+1)
    adj_matrix = [amount_arr for _ in range(len(coins)+1)]

    """
        i => represents the *coin*
        j => represents the *amount*
    """

    for j in range(0, amount+1):
        # no coins left, but there are amounts left? there is no way to make this change = 0.
        adj_matrix[0][j] = 0

    for i in range(0, len(coins)+1):
        # for any current coin (regardless of what it is), if you have 0 amount, then you made the change = 1.
        adj_matrix[i][0] = 1


    for i in range(1, len(coins)+1):
        for j in range(1, amount+1):
            if coins[i-1] <= j:
                adj_matrix[i][j] = adj_matrix[i][j-coins[i-1]] + adj_matrix[i-1][j] # include coin + exclude coin
            else:
                adj_matrix[i][j] = adj_matrix[i-1][j]  # this coin is not applicable; revert back to last known coin

    return adj_matrix[len(coins)][amount]
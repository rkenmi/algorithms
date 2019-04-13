def find_max_min_path(M):
    n = len(M)
    m = len(M[0])
    result = -float('inf')

    def _find_max_min(i, j, min_so_far):
        if i >= m or j >= n:
            return

        curr_min = min(M[j][i], min_so_far)
        nonlocal result

        if i == m-1 and j == n-1:
            result = max(result, curr_min)
            return

        _find_max_min(i+1, j, curr_min)
        _find_max_min(i, j+1, curr_min)

    _find_max_min(0, 0, float('inf'))

    return result

def find_max_min_dp(M):
    n = len(M)
    m = len(M[0])

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = M[0][0]

    for i in range(1, m):
        dp[0][i] = min(M[0][i], dp[0][i-1])

    for j in range(1, n):
        dp[j][0] = min(M[j][0], dp[j-1][0])

    for i in range(1, m):
        for j in range(1, n):
            dp[j][i] = min(max(dp[j-1][i], dp[j][i-1]), M[j][i])

    return dp[n-1][m-1]



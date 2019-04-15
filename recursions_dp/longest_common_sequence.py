def find_lcs(s1, s2):

    def _find_lcs(i, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            return 1 + _find_lcs(i-1, j-1)
        else:
            return max(_find_lcs(i-1, j), _find_lcs(i, j-1))

    return _find_lcs(len(s1)-1, len(s2)-1)


def find_lcs_top_down_dp(s1, s2):
    cache = [[None] * len(s2) for _ in range(len(s1))]

    def _find_lcs(i, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            if cache[i][j] is not None:
                return 1 + cache[i][j]
            else:
                return 1 + _find_lcs(i-1, j-1)
        else:
            if cache[i-1][j] is not None:
                without_i = cache[i-1][j]
            else:
                without_i = _find_lcs(i-1, j)

            if cache[i][j-1] is not None:
                without_j = cache[i][j-1]
            else:
                without_j = _find_lcs(i, j-1)

            return max(without_i, without_j)

    return _find_lcs(len(s1)-1, len(s2)-1)


def find_lcs_bot_down_dp(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * n for _ in range(m)]

    for i in range(0, n):
        dp[0][i] = 1 if s2[0] == s1[i] else 0
        if i > 0:
            dp[0][i] = max(dp[0][i-1], dp[0][i])

    for j in range(0, m):
        dp[j][0] = 1 if s1[0] == s2[j] else 0
        if j > 0:
            dp[j][0] = max(dp[j-1][0], dp[j][0])

    for j in range(1, m):
        for i in range(1, n):
            matches = s2[j] == s1[i]
            dp[j][i] = max(dp[j-1][i], dp[j][i-1]) + matches

    return dp[m-1][n-1]

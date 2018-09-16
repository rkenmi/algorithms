def levenshtein_dp(str1, str2):
    """
    :param str1:
    :param str2:
    :return:
    """
    if not str1 and not str2:
        return 0

    if not str1 or not str2:
        return max(len(str1), len(str2))

    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i > 0 and j > 0 and str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                left, up = 0, 0
                if i > 0:
                    left = dp[i-1][j]
                if j > 0:
                    up = dp[i][j-1]

                if i > 0 or j > 0:
                    dp[i][j] = 1 + min(left, up)

    return dp[len(str1)][len(str2)]

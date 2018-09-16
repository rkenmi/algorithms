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
    for i in range(0, len(str1)+1):
        dp[i][0] = i

    for j in range(0, len(str2)+1):
        dp[0][j] = j

    for i in range(0, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                left = dp[i-1][j]
                up = dp[i][j-1]
                upleft = dp[i-1][j-1]

                dp[i][j] = 1 + min(left, up, upleft)

    return dp[len(str1)][len(str2)]

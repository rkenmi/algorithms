
def deletion_distance(str1, str2):

    if not str1 and not str2:
        return 0

    if not str1 or not str2:
        return len(str1 or str2)

    if str1[-1] != str2[-1]:
        return 1 + min(deletion_distance(str1[:-1], str2), deletion_distance(str1, str2[:-1]))
    else:
        return deletion_distance(str1[:-1], str2[:-1])


def deletion_distance_dp(str1, str2):
    """
    Recurrence relation:

    dist(i, 0) = size of i
    dist(0, j) = size of j

    When i[-1] == j[-1]
    dist(i, j) = min(dist(i-1, j), dist(i, j-1)) + 1

    When i[-1] != j[-1]
    dist(i, j) = dist(i-1, j-1)

    :param str1:
    :param str2:
    :return:
    """
    if not str1 and not str2:
        return 0

    if not str1 or not str2:
        return max(len(str1), len(str2))

    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    return dp[len(str1)][len(str2)]


def deletion_distance_dp_faster(str1, str2):
    """
    Recurrence relation:

    dist(i, 0) = size of i
    dist(0, j) = size of j

    When i[-1] == j[-1]
    dist(i, j) = min(dist(i-1, j), dist(i, j-1)) + 1

    When i[-1] != j[-1]
    dist(i, j) = dist(i-1, j-1)

    :param str1:
    :param str2:
    :return:
    """
    if not str1 and not str2:
        return 0

    if not str1 or not str2:
        return max(len(str1), len(str2))

    dp = [0] * (len(str2)+1)
    last = [0] * (len(str2)+1)

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    return dp[len(str1)][len(str2)]


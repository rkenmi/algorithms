def longest_increasing_subsequence(A):
    dynamic_arr = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(0, i):
            if A[j] <= A[i]:
                dynamic_arr[i] = max(dynamic_arr[i], dynamic_arr[j] + 1)

    return dynamic_arr[-1]


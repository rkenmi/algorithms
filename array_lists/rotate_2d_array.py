def rotate_2d_array(A):
    for j in range(0, len(A) - 2):
        for i in range(j, len(A) - 1 - j):
            old = A[j][i]
            # Preserve the old value of new block and overwrite the old value with the previous preserved value
            A[i][~j], old = old, A[i][~j]
            A[~j][~i], old = old, A[~j][~i]
            A[~i][j], old = old, A[~i][j]

            A[j][i] = old

    return A

def rotate_2d_array_brute_force(A):
    copy = [[0] * len(A) for _ in range(0, len(A))]

    for j in range(0, len(A)):
        for i in range(0, len(A)):
            copy[i][j] = A[~j][i]

    return copy

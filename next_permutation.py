def next_permutation(A):
    sort_point = -1
    for i in reversed(range(len(A)-1)):
        if A[i] < A[i+1]:
            sort_point = i
            break

    counter = sort_point + 1
    min_val = len(A)
    while counter < len(A):
         if A[counter] > A[sort_point] and A[counter] < min_val:
             min_i = counter
             min_val = min(A[counter], min_val)
         counter += 1

    A[min_i], A[sort_point] = A[sort_point], A[min_i]

    A[sort_point+1:] = reversed(sorted(A[sort_point+1:]))


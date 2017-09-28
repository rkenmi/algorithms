
# def remove_replace(A, size):
#     for i in range(size):
#         if A[i] == 'b':
#             A.pop(i)
#             i -= 1
#
#     for i in range(size):
#         if A[i] == 'a':
#             A[i] = 'd'
#             A.insert(i+1, 'd')
#             i += 1


def remove_replace(A, size):
    temp = []
    for i in range(size):
        if A[i] == 'b':
            continue

        if A[i] == 'a':
            temp.append('d')
            temp.append('d')
        else:
            temp.append(A[i])

    A[:size] = temp


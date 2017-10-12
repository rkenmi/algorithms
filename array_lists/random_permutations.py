import random


def random_permutations(k, A):

    for i in range(k):
        swap_ind = random.randint(i, len(A)-1)
        A[i], A[swap_ind] = A[swap_ind], A[i]


def uniform_random_permutations(n):
    A = [i for i in range(n)]
    random_permutations(n, A)
    return A


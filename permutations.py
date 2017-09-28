# BRUTE FORCE WAY => Time is O(n), Space is O(n) extra
def permutations(A, P):
    buffer = [0] * len(A)
    for i in range(0, len(A)):
        buffer[P[i]] = A[i]

    # for i in range(0, len(A)):
    #     A[i] = buffer[i]
    A[:] = buffer
    # A = buffer


# FASTER? => Time is O(n), Space is constant
def permutations2(A, P):
    for i in range(0, len(A)):
        next = i

        while P[next] >= 0:
            # For debugging
            print('i = {} \ta = [{}]\tp = [{}]'.format(str(i),
                                                       " ".join(A),
                                                       " ".join([str(x) for x in P])))
            A[i], A[P[next]] = A[P[next]], A[i]
            temp = P[next]
            P[next] -= len(A)  # this guarantees that we'll have a negative number, since any elem in P < len(A) or len(P)
            next = temp
    P[:] = [n + len(P) for n in P]

"""
[1, 3, 0, 2]    [a, b, c, d]
[-3, 3, 0, 2]   [b, a, c, d]
    iterate thru negative values
    [-3], j starts at 0
        P[j] += 4 (until positive)
        P[j] eventually becomes 1
        if current i == P[j]
            then switch the two


[-3, -1, -4, 2]  [c, d, b, a]
[-3, -1, -4, -2]  [c, a, b, d]


"""


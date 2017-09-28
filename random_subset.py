import random


def random_subset(n, k):
    d = {}

    for i in range(k):
        r = random.randint(i, n)
        r_mapped = d.get(r, r)
        i_mapped = d.get(i, i)

        d[r_mapped], d[i_mapped] = i_mapped, r_mapped

    return [d.get(i) for i in range(k)]


def test_random_subset(n):
    # FIXED k = 4
    k_arr = [28, 42, 28, 64]

    d = {}

    k_arr.reverse()
    for i in range(4):
        r = k_arr.pop()
        r_mapped = d.get(r, r)
        i_mapped = d.get(i, i)

        d[r], d[i] = i_mapped, r_mapped


    return [d.get(i) for i in range(4)]

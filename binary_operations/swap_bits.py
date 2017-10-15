def swap_bits_xor(n, i, j):
    """
    Given a 64-bit integer n, swap bits i and j
    This function makes use of xor logic.
    :param n: Integer
    :param i: Integer
    :param j: Integer
    :return:
    """
    # the two bits i and j are different
    if (n >> i) & 1 != (n >> j) & 1:
        # mark 1 at both i and j on the mask
        bitmask = 1 << i | 1 << j

        # XOR with n
        n ^= bitmask

    return n


def swap_bits(n, i, j):
    """
    Given a 64-bit integer n, swap bits i and j
    This function doesn't use xor logic and its a bit messier.
    :param n: Integer
    :param i: Integer
    :param j: Integer
    :return:
    """
    i_bits = n & (1 << i)
    j_bits = n & (1 << j)

    if i_bits > 0 and j_bits is 0:
        # turn on the jth bit
        n |= (1 << j)

        # kill the ith bit
        n &= ~(1 << i)
    elif j_bits > 0 and i_bits is 0:
        # turn on the ith bit
        n |= (1 << i)

        # kill the jth bit
        n &= ~(1 << j)

    return n


"""
Search if a key exists in a 2d matrix called M

Returns True or False
"""
def search_2d(M, key):
    if not M:
        return False

    start_x = len(M[0]) - 1
    start_y = 0

    while start_y < len(M) and start_x >= 0:
        val = M[start_y][start_x]
        if val == key:
            return True

        if val > key:  # this column is no good... check left of row
            start_x -= 1
        else:  # val < key, so going down this column
            start_y += 1

    return False


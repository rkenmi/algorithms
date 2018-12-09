
def compute_enclosed(A):
    from collections import deque
    n = len(A)  # vertical boundaries
    m = len(A[0])  # horizontal boundaries

    q = deque(
        [(j, k) for i in range(0, n) for j, k in ((0, i), (m-1, i))] +  # vertical boundaries
        [(j, k) for i in range(0, m) for j, k in ((i, 0), (i, n-1))] # horizontal boundaries
    )

    while q:
        x, y = q.popleft()

        if x >= 0 and x < m and y >= 0 and y < n and A[y][x] == 'W':
            A[y][x] = 'Traversed'

            for d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                q.append((x + d[0], y + d[1]))

    A[:] = [['W' if e == 'Traversed' else 'B' for e in row] for row in A]
    return A

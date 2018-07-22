def rotate_2d_array(arr):
    if len(arr) == 0:
        return arr

    if len(arr) != len(arr[0]):
        return arr

    begin, end, laps = 0, len(arr), len(arr)-1
    while begin < end:
        print(begin, end)
        for _ in range(0, laps):
            old = arr[begin+1][begin]
            for i in range(begin, end):
                arr[begin][i], old = old, arr[begin][i]
            print(arr)

            for i in range(begin + 1, end):
                arr[i][end - 1], old = old, arr[i][end - 1]
            print(arr)

            for i in range(begin + 1, end):
                arr[end - 1][end - 1 - i], old = old, arr[end - 1][end - 1 - i]
            print(arr)
            print(begin, end)
            for i in range(begin + 1, end - 1):
                arr[end - 1 - i][begin], old = old, arr[end - 1 - i][begin]

        print(arr)
        laps -= 2
        begin += 1
        end -= 1

    return arr

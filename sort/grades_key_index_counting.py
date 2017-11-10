"""
    Implement key index counting, given an array of characters representing school grades (letters A-F, excluding E)
"""

def grades_key_index_counting(A):
    R = 5  # Number of distinct characters allowed, A, B, C, D, F
    # A = map(ord, list(D.keys()))  # convert char to its integer value (unicode in py3, ascii in py2)
    count = [0] * (R+1)  # count[0] will be reserved

    grade_map = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4
    }

    # First stage: Count frequencies of the integer values
    for grade in A:
        count[grade_map[grade]+1] += 1

    # Second stage: Accumulate the count array with the running sums
    running_sum = 0
    for i in range(len(count)):
        running_sum += count[i]
        count[i] = running_sum

    sorted_A = [0] * len(A)
    # Third stage: Traverse the original A, read a value and use the count array to determine its new placement
    for grade in A:
        sorted_A[count[grade_map[grade]]] = grade
        count[grade_map[grade]] += 1  # increment index to prevent collisions

    return sorted_A




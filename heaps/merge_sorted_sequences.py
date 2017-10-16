import collections
import heapq


def merge_sorted_sequences_naive(sequences):
    # doesn't actually use heaps, but its the easiest way
    result = []
    for seq in sequences:
        result.extend(seq)

    return sorted(result)


def merge_sorted_sequences_iters(sequences):
    """
    Cleaner Iterator variation
    :param sequences:
    :return:
    """
    sequences_iters = [iter(seq) for seq in sequences]
    heap = []
    for i, seq in enumerate(sequences_iters):
        first_elem = next(seq, None)
        if first_elem is not None:
            # add pairs into the heap, by default the first element is used as sorting key
            heapq.heappush(heap, (first_elem, i))

    result = []
    while heap:
        # gets the min pair, and we need that because that's what will be popped later
        iter_index = heap[0][1]

        iterator = sequences_iters[iter_index]
        next_elem = next(iterator, None)
        if next_elem is not None:
            heapq.heappush(heap, (next_elem, iter_index))
        result.append(heapq.heappop(heap)[0])

    return result


def merge_sorted_sequences_indexing(sequences):
    """
    Non-iterator variation. Uses a 3-tuple to store the sequence counter for each sequence.
    :param sequences:
    :return:
    """
    Element = collections.namedtuple("Element", ["value", "sequence_index", "sequence_counter"])
    heap = []
    for i, seq in enumerate(sequences):
        if seq:
            # add pairs into the heap, by default the first element is used as sorting key
            heapq.heappush(heap, Element(seq[0], i, 1))  # sequence counter starts at 1

    result = []
    while heap:
        # gets the min pair, and we need that because that's what will be popped later
        elem = heap[0]

        sequence = sequences[elem.sequence_index]
        if elem.sequence_counter < len(sequence):
            next_value = sequence[elem.sequence_counter]
            heapq.heappush(heap, Element(next_value, elem.sequence_index, elem.sequence_counter + 1))
        result.append(heapq.heappop(heap).value)

    return result

def merge(sequences):
    """
    Based on merge sort's merge.
    This isn't a heap based algorithm, but it's a nice algorithm to compare and contrast to.
    Merge should have similar time complexity to heap based sort => O(n log n)
    However merge requires n space to be allocated. Heaps only require k, for k is the # of sequences.
    :param sequences:
    :return:
    """

    def _merge(A, B):
        # space = [0] * (len(A) + len(B))
        space_counter = 0

        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                space[space_counter] = A[i]
                i += 1
            else:
                space[space_counter] = B[j]
                j += 1

            space_counter += 1

        while i < len(A):
            space[space_counter] = A[i]
            i +=  1
            space_counter += 1

        while j < len(B):
            space[space_counter] = B[j]
            j +=  1
            space_counter += 1

        return space[0:len(A)+len(B)]


    k = 0
    offset = 1
    max_size = 0

    for seq in sequences:
        max_size += len(seq)

    space = [0] * max_size

    """
    [x x x x x x x]
    [y x y x y x y]
    [z x y x z x y]
    [G x y x z x y]
    """
    while offset < len(sequences):
        while k + offset < len(sequences):
            sequences[k] = _merge(sequences[k], sequences[k+offset])
            k += (offset * 2)
        offset *= 2
        k = 0

    return sequences[0]

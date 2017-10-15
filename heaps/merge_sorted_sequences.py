import heapq


def merge_sorted_sequences_naive(sequences):
    # doesn't actually use heaps, but its the easiest way
    result = []
    for seq in sequences:
        result.extend(seq)

    return sorted(result)

def merge_sorted_sequences(sequences):
    heap = []
    max_index = 0
    for seq in sequences:
        if len(seq) > 0:  # if seq isn't empty
            heapq.heappush(heap, seq[0])
        max_index = max(max_index, len(seq))

    i = 1
    result = []
    while i < max_index:  # this is O(n * log n) despite the 2 nested loops. log n comes from heappushpop.
        for seq in sequences:
            if i < len(seq):
                # keep heap at most size k, for k = # of sequences
                result.append(heapq.heappushpop(heap, seq[i]))  # note the push THEN pop
        i += 1

    while len(heap) > 0:  # while heap isn't empty
        result.append(heapq.heappop(heap))

    return result


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
        if first_elem:
            # add pairs into the heap, by default the first element is used as sorting key
            heapq.heappush(heap, (first_elem, i))

    result = []
    while heap:
        # gets the min pair, and we need that because that's what will be popped later
        iter_index = heap[0][1]

        iterator = sequences_iters[iter_index]
        next_elem = next(iterator, None)
        if next_elem:
            result.append(heapq.heappushpop(heap, (next_elem, iter_index))[0])
        else:
            result.append(heapq.heappop(heap)[0])

    return result



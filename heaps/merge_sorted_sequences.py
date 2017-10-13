import heapq

from Algorithm import Algorithm


def merge_sorted_sequences(sequences):
    heap = []
    max_index = 0
    for seq in sequences:
        if len(seq) > 0:  # if seq isn't empty
            heapq.heappush(heap, seq[0])
        max_index = max(max_index, len(seq))

    i = 1
    result = []
    while i < max_index:
        for seq in sequences:
            if i < len(seq):
                # keep heap at most size k, for k = # of sequences
                result.append(heapq.heappushpop(heap, seq[i]))
        i += 1

    while len(heap) > 0:  # while heap isn't empty
        result.append(heapq.heappop(heap))

    return result

class MergeSortedSequences(Algorithm):
    pass

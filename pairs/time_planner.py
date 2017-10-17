"""
    Key takeaway is look at your inputs carefully. Realize that it is sorted and take advantage of it.
"""
import heapq


def time_planner_naive(slotsA, slotsB, dur):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param slotsA: Sorted time slots represented as lists => [start, end]
    :param slotsB: Sorted time slots represented as lists => [start, end]
    :param dur: Duration of meeting for both users A and B
    :return: The appointment of the meeting represented as a list => [start, end],
                otherwise None if no meeting can be made
    """
    for slotA in slotsA:
        if slotA[1] - slotA[0] >= dur:
            for slotB in slotsB:
                start = max(slotB[0], slotA[0])
                end = min(slotB[1], slotA[1])
                if end - start >= dur:
                    return [start, start + dur]
    return None


def time_planner(slotsA, slotsB, dur):
    """
    Time Complexity: O(n log k) where k is the # of sequences (just 2 in this case for slotsA and slotsB)
    Space Complexity: O(k)
    :param slotsA: Sorted time slots represented as lists => [start, end]
    :param slotsB: Sorted time slots represented as lists => [start, end]
    :param dur: Duration of meeting for both users A and B
    :return: The appointment of the meeting represented as a list => [start, end],
                otherwise None if no meeting can be made
    """
    slotsAB = heapq.merge(slotsA, slotsB)
    prev_slot = None
    for slot in slotsAB:
        if prev_slot is not None:
            start = max(slot[0], prev_slot[0])
            end = min(slot[1], prev_slot[1])
            if end - start >= dur:
                return [start, start + dur]
        prev_slot = slot
    return None


def time_planner_fast(slotsA, slotsB, dur):
    """
    Time Complexity: O(N + M), where N is the elements in slotsA, M is the elements in slotsB
    Space Complexity: O(1)
    :param slotsA: Sorted time slots represented as lists => [start, end]
    :param slotsB: Sorted time slots represented as lists => [start, end]
    :param dur: Duration of meeting for both users A and B
    :return: The appointment of the meeting represented as a list => [start, end],
                otherwise None if no meeting can be made
    """
    if not slotsA or not slotsB:
        return None

    i, j = 0, 0
    while i < len(slotsA) and j < len(slotsB):
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])
        if end - start >= dur:
            return [start, start + dur]

        if slotsA[i][0] < slotsB[j][0]:
            i += 1
        else:
            j += 1

    return None


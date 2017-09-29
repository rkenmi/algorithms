import collections


def has_cycle(head):
    slow = fast = head
    while slow and slow.next and fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            temp = slow
            count = 0
            while temp:
                temp = temp.next
                count += 1
                if temp == slow:
                    break

            loop_start = head
            for _ in range(count):
                loop_start = loop_start.next

            start = head
            while loop_start != start:
                loop_start = loop_start.next
                start = start.next

            return loop_start

def does_overlap(ll_a, ll_b):
    exists = collections.defaultdict(bool)

    while ll_a:
        exists[ll_a] = True  # assumes that linked list nodes can be represented uniquely as a key string
        ll_a = ll_a.next

    while ll_b:
        if exists[ll_b]:
            return True

    return False

def does_overlap_fast(ll_a, ll_b):

    def count(llist):
        c = 0
        while llist:
            llist = llist.next
            c += 1
        return c

    ll_a_count = count(ll_a)
    ll_b_count = count(ll_b)  # assume ll_b is greater in size
    diff = abs(ll_a_count - ll_b_count)

    # if ll_a is actually greater, then swap linked lists so that ll_b is greater as assumed above
    if ll_a_count > ll_b_count:
        ll_a, ll_b = ll_b, ll_a

    for _ in range(diff):  # move forward by offset on the larger linked list
        ll_b = ll_b.next

    while ll_a and ll_b:  # since ll_b is moved by offset, these two ptrs will reach null at the same time
        if ll_a == ll_b:
            return ll_a
        ll_a = ll_a.next
        ll_b = ll_b.next

    return None


def does_overlap_w_cycles(ll_a, ll_b):
    """
    Handles detection of linked lists with cycles and returns the starting node of the cycle.

    i.e.

    ll_a: A -> B -> C -> D -> E -> C -> D -> E ...

    ll_b: F -> D -> E -> C -> D -> E -> C ...

    In this case, the node to return can be C or D, because ll_a's first instance of a cycle was C, where
    as ll_b's first instance of a cycle was D.

    :param ll_a:
    :param ll_b:
    :return: None if no cycle, otherwise the start of a cycle
    """
    def count_to(a, b):
        counter = 0
        while a != b:
            a = a.next
            counter += 1
        return counter

    ll_a_cycle = has_cycle(ll_a)
    ll_b_cycle = has_cycle(ll_b)

    if not ll_a_cycle and not ll_b_cycle:
        return does_overlap_fast(ll_a, ll_b)
    elif (ll_a_cycle and not ll_b_cycle) or (ll_b_cycle and not ll_a_cycle):  # if one list is cyclic and other is not, there is no overlap
        return None

    """
    if ll_a and ll_b are both cyclic,
    then either:
    
    - they go to the same shared cycle at the same entrance node
        - find where the cycle starts
    - they go to the same shared cycle at a different entrance node (like in example above)
        - return either starting location (of list a or list b)
    - they have different cycles altogether; no overlap
        - return None (how to check?)
    """


    temp = ll_b_cycle
    while True:
        temp = temp.next
        if temp == ll_a_cycle or temp == ll_b_cycle:
            break

    # temp made a loop around the cycle back to itself and never touched ll_a_cycle
    # this means that the two cycles associated with ll_a_cycle and ll_b_cycle are disjoint; no overlap
    if temp != ll_a_cycle:
        return None

    # at this point, we know that the two cycles are shared at a certain point
    # but, its possible that these two lists share an overlapping node before the cycles

    dist_a = count_to(ll_a, ll_a_cycle)
    dist_b = count_to(ll_b, ll_b_cycle)

    # let b be the bigger linked list, if not, then swap the linked lists to reflect that
    if dist_b < dist_a:
        ll_a, ll_b = ll_b, ll_a
        ll_a_cycle, ll_b_cycle = ll_b_cycle, ll_a_cycle

    # we want to move the bigger linked list by the offset of the difference of distances, so that
    # ll_a hits the cycle of ll_a at the same time ll_b hits the cycle of ll_b.
    for _ in range(abs(dist_a - dist_b)):
        ll_b = ll_b.next

    # loop will stop as soon as ll_a is the same as ll_b, meaning an early overlap is found.
    # or when either ll_a or ll_b hits their cycle (they should reach their cycles at the same time)
    while ll_a is not ll_a_cycle and ll_b is not ll_b_cycle and ll_a is not ll_b:
        ll_a  = ll_a.next
        ll_b = ll_b.next

    if ll_a == ll_b:  # if they match, then an earlier overlap is found before the cycle (or maybe even at the cycle)
        return ll_a

    # return the starting location of list a or list b; list a is picked here
    return ll_a_cycle











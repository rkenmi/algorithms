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
            return True
        ll_a = ll_a.next
        ll_b = ll_b.next

    return False





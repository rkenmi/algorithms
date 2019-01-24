def merge_two_sorted_lists(L1, L2):
    from linked_lists.ListNode import ListNode
    sentinel = tail = ListNode(None)
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next

        tail = tail.next

    remaining = L1 or L2
    if remaining:
        tail.next = remaining

    return sentinel.next

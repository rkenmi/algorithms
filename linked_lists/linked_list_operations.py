def delete(node):
    """
    Deletes a node in a singly linked list in O(1) with a small caveat;
    The input node must not be a tail.

    Traditionally, delete in a SLL costs O(n) time.
    This is more of a fake delete, because the node object's memory address is still the same.
    But objectively speaking, this node will behave as the successor node and it will
    appear as if the linked list has "deleted" the current node.

    :param node: A linked list node that is not a tail node.
    :return: True if success, False otherwise
    """
    node.data = node.next.data
    node.next = node.next.next

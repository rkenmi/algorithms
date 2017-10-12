import collections

from Algorithm import Algorithm


def least_common_ancestor_parents(node1, node2):
    """
    Compute LCA when each node has a pointer to a parent. Root node isn't necessary in this case.
    :param node1:
    :param node2:
    :return:
    """

    def get_depth(node):
        if node is None:
            return -1

        return get_depth(node.parent) + 1


    node1_h = get_depth(node1)
    node2_h = get_depth(node2)

    if node1_h > node2_h:
        # make node1's depth smaller, always
        node1_h, node2_h = node2_h, node1_h
        node1, node2 = node2, node1

    for _ in range(node2_h - node1_h):
        node2 = node2.parent

    while node1 is not node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1


class LeastCommonAncestorParents(Algorithm):
    pass


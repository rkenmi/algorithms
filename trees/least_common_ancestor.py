import collections

from Algorithm import Algorithm


def least_common_ancestor_namedtuple(root, node1, node2):
    Status = collections.namedtuple("Status", ["num_matches", "ancestor"])

    def lca(root, node1, node2):
        if root is None:
            return Status(0, None)

        left = lca(root.left, node1, node2)
        if left.num_matches is 2:
            return left

        right = lca(root.right, node1, node2)
        if right.num_matches is 2:
            return right

        num_matches = left.num_matches + right.num_matches + int(root in (node1, node2))
        return Status(num_matches, root if num_matches == 2 else None)

    return lca(root, node1, node2).ancestor


def least_common_ancestor(root, node1, node2):
    if root is None:
        return None

    if root is node1 or root is node2:
        return root
    else:
        left = least_common_ancestor(root.left, node1, node2)
        right = least_common_ancestor(root.right, node1, node2)
        if left and right:
            return root  # root must be the ancestor if left and right both point to a node respectively
        elif left or right:
            return left or right  # if only one child is a match, return that child


class LeastCommonAncestor(Algorithm):
    pass


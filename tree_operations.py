import collections

from Tree import BinaryTree
from Tree import sample, symmetric_tree

import math

def is_height_balanced_slow(tree):
    lookup = {}

    def check_height_balance(tree):
        if not tree:
            return 0

        left_count = check_height_balance(tree.left)
        right_count = check_height_balance(tree.right)

        hi = max(left_count, right_count)
        lo = min(left_count, right_count)

        lookup[tree] = hi - lo
        return hi + 1

    check_height_balance(tree)
    for v in lookup.values():
        if v > 1:
            return False

    return True

def is_height_balanced(tree):
    def check_height_balance(tree):
        if not tree:
            return 0

        left_count = check_height_balance(tree.left)
        right_count = check_height_balance(tree.right)
        hi = max(left_count, right_count)
        lo = min(left_count, right_count)

        if hi - lo > 1:
            return math.inf
        else:
            return hi + 1

    return False if check_height_balance(tree) is math.inf else True


def is_height_balanced_ntuples(tree):
    BalancedTree = collections.namedtuple(
        'BalancedTree', ('height', 'is_balanced')
    )

    def check_height_balance(tree):
        if not tree:
            return BalancedTree(0, True)

        left_subtree = check_height_balance(tree.left)
        if not left_subtree.is_balanced:
            return BalancedTree(0, False)

        right_subtree = check_height_balance(tree.right)
        if not right_subtree.is_balanced:
            return BalancedTree(0, False)

        is_balanced = abs(left_subtree.height - right_subtree.height) <= 1
        height = max(left_subtree.height, right_subtree.height) + 1
        return BalancedTree(height, is_balanced)

    return check_height_balance(tree).is_balanced

def is_symmetric(tree):

    def are_subtrees_symmetric(node_a, node_b):
        # base case: when both nodes are null
        if node_a is None and node_b is None:
            return True

        # skip the symmetric null objs and consider only the non-null objs
        if node_a.left is None and node_b.right is None:
            return are_subtrees_symmetric(node_b.left, node_a.right)
        elif node_a.right is None and node_b.left is None:
            return are_subtrees_symmetric(node_b.right, node_a.left)
        # children nodes are symmetrical
        elif node_a.left and node_b.right and node_a.left.data == node_b.right.data \
                and node_a.right and node_b.left and node_a.right.data == node_b.left.data:
            return are_subtrees_symmetric(node_a.left, node_b.right) and are_subtrees_symmetric(node_b.left, node_a.right)

        return False

    if tree.left.data is tree.right.data:
        return are_subtrees_symmetric(tree.left, tree.right)
    return False

import collections

from copy import deepcopy

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

    def are_subtrees_symmetric(tree_l, tree_r):
        if not tree_l and not tree_r:
            return True

        if tree_l and tree_r and tree_l.data is tree_r.data:
            return are_subtrees_symmetric(tree_l.left, tree_r.right) and \
                   are_subtrees_symmetric(tree_l.right, tree_r.left)

        return False


    return are_subtrees_symmetric(tree.left, tree.right)

def is_symmetric_naive(tree):

    def mirrorize_tree(tree):
        if tree is None:
            return

        tree.left, tree.right = tree.right, tree.left
        mirrorize_tree(tree.left)
        mirrorize_tree(tree.right)

    def equals_tree(tree1, tree2):
        if not tree1 and not tree2:
            return True

        if tree1 and tree2 and tree1.data is tree2.data:
            return equals_tree(tree1.left, tree2.left) and equals_tree(tree1.right, tree2.right)

        return False

    mirror_tree = deepcopy(tree)
    mirrorize_tree(mirror_tree)
    return equals_tree(tree, mirror_tree)

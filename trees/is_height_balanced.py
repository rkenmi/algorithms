import collections

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

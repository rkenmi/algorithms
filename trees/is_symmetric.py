from copy import deepcopy


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

    mirror_tree = deepcopy(tree)  # O(n) space for n nodes in the tree
    mirrorize_tree(mirror_tree)  # O(log n)
    return equals_tree(tree, mirror_tree)  #  O(n) time



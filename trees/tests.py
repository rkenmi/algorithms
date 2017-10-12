import unittest

from trees.least_common_ancestor import least_common_ancestor
from trees.Tree import BinaryTree
from trees.is_symmetric import is_symmetric

class Trees(unittest.TestCase):

    def build_basic_tree(self):
        sample = BinaryTree(0)
        sample.left = BinaryTree(1)
        sample.right = BinaryTree(2)
        sample.left.left = BinaryTree(3)
        sample.left.right = BinaryTree(4)
        sample.left.left.left = BinaryTree(5)
        return sample

    def build_symmetric_tree(self):
        symmetric_tree = BinaryTree(0)
        symmetric_tree.left = BinaryTree(1)
        symmetric_tree.left.left = BinaryTree(2)
        symmetric_tree.left.left.right = BinaryTree(3)
        symmetric_tree.left.left.left = BinaryTree(4)
        symmetric_tree.right = BinaryTree(1)
        symmetric_tree.right.right = BinaryTree(2)
        symmetric_tree.right.right.left = BinaryTree(3)
        symmetric_tree.right.right.right = BinaryTree(4)
        return symmetric_tree

    def build_unsymmetric_tree(self):
        symmetric_tree = BinaryTree(0)
        symmetric_tree.left = BinaryTree(1)
        symmetric_tree.left.left = BinaryTree(1)
        symmetric_tree.left.left.right = BinaryTree(3)
        symmetric_tree.left.left.left = BinaryTree(4)
        symmetric_tree.right = BinaryTree(1)
        symmetric_tree.right.right = BinaryTree(2)
        symmetric_tree.right.right.left = BinaryTree(3)
        symmetric_tree.right.right.right = BinaryTree(4)
        return symmetric_tree

    def test_symmetry(self):
        symmetric_tree = self.build_symmetric_tree()
        unsymmetric_tree = self.build_basic_tree()
        self.assertEqual(True, is_symmetric(symmetric_tree))
        self.assertEqual(False, is_symmetric(unsymmetric_tree))

        unsymmetric_tree = self.build_unsymmetric_tree()
        self.assertEqual(False, is_symmetric(unsymmetric_tree))

    def test_lca(self):
        tree = self.build_basic_tree()
        self.assertEqual(tree.left, least_common_ancestor(tree, tree.left.left, tree.left.right))
        self.assertEqual(tree, least_common_ancestor(tree, tree.left.left, tree.right))
        self.assertEqual(tree.left.left, least_common_ancestor(tree, tree.left.left.left, tree.left.left))


if __name__ == '__main__':
    unittest.main()

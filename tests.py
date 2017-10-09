import unittest

from Tree import BinaryTree
from longest_increasing_subsequence import longest_increasing_subsequence
from tree_operations import is_symmetric


class Lists(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        self.assertEquals(6, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))
        self.assertEquals(2, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))

class Trees(unittest.TestCase):

    def build_tree(self):
        sample = BinaryTree(0)
        sample.left = BinaryTree(1)
        sample.right = BinaryTree(2)
        sample.left.left = BinaryTree(3)
        sample.left.right = BinaryTree(4)
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


    def test_symmetry(self):
        symmetric_tree = self.build_symmetric_tree()
        unsymmetric_tree = self.build_tree()
        self.assertEqual(True, is_symmetric(symmetric_tree))
        self.assertEqual(False, is_symmetric(unsymmetric_tree))


if __name__ == '__main__':
    unittest.main()

import unittest

from trees.Tree import BinaryTree, BinarySearchTree
from trees.get_height import get_height
from trees.is_symmetric import is_symmetric
from trees import least_common_ancestor, get_kth_smallest_bst, get_kth_largest_bst, lca_bst
from trees import least_common_ancestor_parents
from utils import algorithms


class BinaryTrees(unittest.TestCase):

    def build_basic_tree(self):
        sample = BinaryTree(0)
        sample.left = BinaryTree(1)
        sample.right = BinaryTree(2)
        sample.left.left = BinaryTree(3)
        sample.left.right = BinaryTree(4)
        sample.left.left.left = BinaryTree(5)
        return sample

    def build_basic_tree_parents(self):
        sample = BinaryTree(0)
        sample.left = BinaryTree(1)
        sample.left.parent = sample
        sample.right = BinaryTree(2)
        sample.right.parent = sample
        sample.left.left = BinaryTree(3)
        sample.left.left.parent = sample.left
        sample.left.right = BinaryTree(4)
        sample.left.right.parent = sample.left
        sample.left.left.left = BinaryTree(5)
        sample.left.left.left.parent = sample.left.left
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
        for algo in algorithms(least_common_ancestor):
            self.assertEqual(tree.left, algo(tree, tree.left.left, tree.left.right))
            self.assertEqual(tree, algo(tree, tree.left.left, tree.right))
            self.assertEqual(tree.left.left, algo(tree, tree.left.left.left, tree.left.left))

    def test_lca_parents(self):
        tree = self.build_basic_tree_parents()
        for algo in algorithms(least_common_ancestor_parents):
            self.assertEqual(tree.left,algo(tree.left.left, tree.left.right))
            self.assertEqual(tree, algo(tree.left.left, tree.right))
            self.assertEqual(tree.left.left, algo(tree.left.left.left, tree.left.left))


class BinarySearchTrees(unittest.TestCase):
    def build_basic_tree(self):
        sample = BinarySearchTree(3)
        sample.add(BinaryTree(2))
        sample.add(BinaryTree(4))
        sample.add(BinaryTree(1))
        sample.add(BinaryTree(5))
        return sample

    def build_big_tree(self):
        sample = BinarySearchTree(10)
        sample.add(BinaryTree(3))
        sample.add(BinaryTree(50))
        sample.add(BinaryTree(20))
        sample.add(BinaryTree(35))
        sample.add(BinaryTree(55))
        sample.add(BinaryTree(15))
        sample.add(BinaryTree(11))
        sample.augment(count=True)
        return sample

    def test_get(self):
        bst = self.build_basic_tree()
        self.assertEqual(5, bst.get(5).data)
        self.assertEqual(None, bst.get(6))

    def test_remove(self):
        bst = self.build_big_tree()
        self.assertEqual(5, get_height(bst))
        self.assertEqual(50, bst.remove(50).data)
        self.assertEqual(3, bst.remove(3).data)
        self.assertEqual(55, bst.remove(55).data)

        self.assertEqual(11, bst.remove(11).data)
        self.assertEqual(4, get_height(bst))

    def test_lca_bst(self):
        bst = self.build_big_tree()
        for algo in algorithms(lca_bst):
            self.assertEqual(bst, algo(bst, bst.left, bst.right))
            self.assertEqual(bst.right, algo(bst, bst.right.left, bst.right.right))
            # a node can be a descendent of itself
            self.assertEqual(bst.right.left, algo(bst, bst.right.left, bst.right.left.right))

    def test_kth_smallest_bst(self):
        bst = self.build_big_tree()
        for algo in algorithms(get_kth_smallest_bst):
            node = algo(bst, 0)
            self.assertEqual(10, node.data)

            node = algo(bst, 1)
            self.assertEqual(3, node.data)

            node = algo(bst, 2)
            self.assertEqual(10, node.data)

            node = algo(bst, 3)
            self.assertEqual(11, node.data)

            node = algo(bst, 4)
            self.assertEqual(15, node.data)

            node = algo(bst, 5)
            self.assertEqual(20, node.data)

            node = algo(bst, 6)
            self.assertEqual(35, node.data)

            node = algo(bst, 7)
            self.assertEqual(50, node.data)

            node = algo(bst, 8)
            self.assertEqual(55, node.data)

    def test_kth_largest_bst(self):
        bst = self.build_big_tree()
        for algo in algorithms(get_kth_largest_bst):
            node = algo(bst, 0)
            self.assertEqual(10, node.data)

            node = algo(bst, 1)
            self.assertEqual(55, node.data)

            node = algo(bst, 2)
            self.assertEqual(50, node.data)

            node = algo(bst, 3)
            self.assertEqual(35, node.data)

            node = algo(bst, 4)
            self.assertEqual(20, node.data)

            node = algo(bst, 5)
            self.assertEqual(15, node.data)

            node = algo(bst, 6)
            self.assertEqual(11, node.data)

            node = algo(bst, 7)
            self.assertEqual(10, node.data)

            node = algo(bst, 8)
            self.assertEqual(3, node.data)

if __name__ == '__main__':
    unittest.main()

import unittest

from stacks_queues.Queue import CircularQueue
from stacks_queues.Stack import Stack
from stacks_queues import well_formed_brackets_stacks, binary_tree_nodes_by_depth
from trees.Tree import BinaryTree
from utils import algorithms


class StacksContainer(unittest.TestCase):
    def test_stack_basic_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())

    def test_stack_max(self):
        s = Stack()
        s.push(1)
        s.push(5)
        s.push(3)

        self.assertEqual(5, s.max())

    def test_stack_max_dupes(self):
        s = Stack()
        s.push(5)
        s.push(5)
        s.push(5)

        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(5, s.max())

        s.push(7)
        s.push(7)

        self.assertEqual(7, s.max())
        s.pop()
        self.assertEqual(7, s.max())
        s.pop()
        self.assertEqual(5, s.max())

    def test_stack_pop_empty(self):
        s = Stack()
        self.assertEqual(True, s.empty())
        self.assertRaises(IndexError, s.pop)

    def test_stack_empty(self):
        s = Stack()
        self.assertEqual(True, s.empty())


class StacksAlgorithms(unittest.TestCase):
    def test_well_formed_brackets(self):
        for algo in algorithms(well_formed_brackets_stacks):
            self.assertEqual(True, algo(""))
            self.assertEqual(False, algo("{"))
            self.assertEqual(False, algo("[)"))
            self.assertEqual(True, algo("[]"))
            self.assertEqual(False, algo("(]"))
            self.assertEqual(True, algo("()[]"))
            self.assertEqual(True, algo("[()]"))
            self.assertEqual(True, algo("[(){}]"))
            self.assertEqual(True, algo("[({})]"))
            self.assertEqual(False, algo("[({)}]"))
            self.assertEqual(False, algo("[({}))]"))
            self.assertEqual(False, algo("[[[]]"))

class QueueAlgorithms(unittest.TestCase):
    def build_basic_tree(self):
        sample = BinaryTree(0)
        sample.left = BinaryTree(1)
        sample.right = BinaryTree(2)
        sample.left.left = BinaryTree(3)
        sample.left.right = BinaryTree(4)
        sample.left.left.left = BinaryTree(5)
        return sample

    def test_binary_nodes_by_depth(self):
        tree = self.build_basic_tree()
        for algo in algorithms(binary_tree_nodes_by_depth):
            out = [[tree], [tree.left, tree.right], [tree.left.left, tree.left.right], [tree.left.left.left]]
            out2 = algo(tree)
            self.assertEqual(out, out2)


class CircularQueues(unittest.TestCase):
    def test_enqueue(self):
        q = CircularQueue(capacity=3)
        q.enqueue(5)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual([5, 2, 3], q.elements)
        self.assertEqual(3, q.size())
        q.enqueue(4)
        self.assertEqual([5, 2, 3, 4, None, None], q.elements)
        self.assertEqual(4, q.size())

    def test_dequeue(self):
        q = CircularQueue(capacity=3)
        q.enqueue(5)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(5, q.dequeue())
        self.assertEqual(2, q.size())
        self.assertEqual([5, 2, 3], q.elements)

        self.assertEqual(2, q.dequeue())
        self.assertEqual(1, q.size())
        self.assertEqual([5, 2, 3], q.elements)

        self.assertEqual(3, q.dequeue())
        self.assertEqual(0, q.size())
        self.assertRaises(IndexError, q.dequeue)

    def test_shifting(self):
        q = CircularQueue(capacity=3)
        q.enqueue(5)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(5, q.dequeue())
        self.assertEqual(2, q.size())
        self.assertEqual([5, 2, 3], q.elements)

        q.enqueue(9)
        self.assertEqual(3, q.size())
        self.assertEqual([9, 2, 3], q.elements)


        self.assertEqual(2, q.dequeue())
        self.assertEqual(3, q.dequeue())
        self.assertEqual(1, q.size())
        self.assertEqual([9, 2, 3], q.elements)

        q.enqueue(7)
        q.enqueue(4)
        self.assertEqual(3, q.size())
        self.assertEqual([9, 7, 4], q.elements)

        q.enqueue(30)
        self.assertEqual([9, 7, 4, 30, None, None], q.elements)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(40)
        self.assertEqual([9, 7, 4, 30, 40, None], q.elements)
        q.enqueue(50)
        self.assertEqual([9, 7, 4, 30, 40, 50], q.elements)
        q.enqueue(60)
        self.assertEqual([60, 7, 4, 30, 40, 50], q.elements)


if __name__ == '__main__':
    unittest.main()

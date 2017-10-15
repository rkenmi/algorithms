import unittest

from stacks.Stack import Stack
from stacks import well_formed_brackets_stacks
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

if __name__ == '__main__':
    unittest.main()

import unittest

from search import binary_search_first
from search import binary_search_cyclic
from utils import algorithms


class BinarySearch(unittest.TestCase):
    def test_binary_search_first_occurence(self):
        for algo in algorithms(binary_search_first):
            self.assertEqual(0, algo([0, 1, 2], 0))
            self.assertEqual(2, algo([0, 1, 2], 2))
            self.assertEqual(5, algo([0, 1, 2, 3, 4, 5, 5, 6, 7], 5))
            self.assertEqual(0, algo([5, 5, 5, 5, 5, 5, 5], 5))
            self.assertEqual(-1, algo([5, 5, 5, 5, 5, 5, 5], 8))

    def test_binary_search_sorted_cyclic_array(self):
        for algo in algorithms(binary_search_cyclic):
            self.assertEqual(1, algo([3, 0, 1, 2]))
            self.assertEqual(3, algo([0, 1, 2, -1]))

if __name__ == '__main__':
    unittest.main()

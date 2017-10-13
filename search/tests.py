import unittest

from search.binary_search_first import BinarySearchFirst


class BinarySearch(unittest.TestCase):
    def test_binary_search_first_occurence(self):
        bs1 = BinarySearchFirst()
        for algo in bs1.get_functions():
            self.assertEqual(0, algo([0, 1, 2], 0))
            self.assertEqual(2, algo([0, 1, 2], 2))
            self.assertEqual(5, algo([0, 1, 2, 3, 4, 5, 5, 6, 7], 5))
            self.assertEqual(0, algo([5, 5, 5, 5, 5, 5, 5], 5))
            self.assertEqual(-1, algo([5, 5, 5, 5, 5, 5, 5], 8))


if __name__ == '__main__':
    unittest.main()

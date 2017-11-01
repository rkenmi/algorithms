import unittest

from sort import merge_sorted_arrays_into_A1, smallest_nonconstructible
from utils import algorithms


class Sorts(unittest.TestCase):
    def test_smallest_nonconstructible(self):
        # 1 2 4:  1 2 3 4 5 6
        # 1 2 5:  1 2 3 5 6 7
        # 1 2 6:  1 2 3 6 7 8
        # 1 3 6:  1 3 4 6 7 9 10
        # 1 3 7:  1 3 4 7 8 10 11
        # 1 3 8:  1 3 4 8 9 11 12
        for algo in algorithms(smallest_nonconstructible):
            self.assertEqual(7, algo([1, 2, 4]))
            self.assertEqual(7, algo([2, 1, 4]))
            self.assertEqual(4, algo([1, 2, 5]))
            self.assertEqual(4, algo([5, 2, 1]))
            self.assertEqual(4, algo([1, 2, 6]))
            self.assertEqual(2, algo([1, 3, 6]))
            self.assertEqual(2, algo([1, 3, 7]))
            self.assertEqual(2, algo([1, 3, 8]))


    def test_merge_into_A1(self):
        for algo in algorithms(merge_sorted_arrays_into_A1):
            self.assertEqual([3, 8, 10], algo([3, 10, None], [8]))
            self.assertEqual([3, 4, 5, 7, 8, 10], algo([3, 10, None, None, None, None], [4, 5, 7, 8]))


if __name__ == '__main__':
    unittest.main()

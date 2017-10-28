import unittest

from sort import merge_sorted_arrays_into_A1
from utils import algorithms


class Sorts(unittest.TestCase):
    def test_merge_into_A1(self):
        for algo in algorithms(merge_sorted_arrays_into_A1):
            self.assertEqual([3, 8, 10], algo([3, 10, None], [8]))
            self.assertEqual([3, 4, 5, 7, 8, 10], algo([3, 10, None, None, None, None], [4, 5, 7, 8]))


if __name__ == '__main__':
    unittest.main()

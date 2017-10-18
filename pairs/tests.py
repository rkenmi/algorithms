import unittest

from pairs import time_planner, exact_difference
from utils import algorithms


class Pairs(unittest.TestCase):
    def test_time_planner(self):
        for algo in algorithms(time_planner):
            self.assertEqual([60, 68], algo([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
            self.assertEqual(None, algo([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
            self.assertEqual([65, 77], algo([[10, 50], [55, 60], [65, 80], [140, 210]], [[0, 15], [60, 100]], 12))

    def test_exact_difference(self):
        for algo in algorithms(exact_difference):
            self.assertEqual([[4, 1]], algo([4, 1], 3))
            self.assertEqual([[4, 1]], algo([4, 2, 1], 3))
            #  use assertCountEqual to check if list contents are identical, except the ordering.
            self.assertCountEqual([[4, 1], [3, 0]], algo([4, 2, 3, 1, 0], 3))
            self.assertCountEqual([[1, 0], [-1, -2], [0, -1], [2, 1]], algo([-2, 1, -1, 0, 2], 1))
            self.assertCountEqual([], algo([], 3))

if __name__ == '__main__':
    unittest.main()

import unittest

from pairs import time_planner
from utils import algorithms


class Pairs(unittest.TestCase):
    def test_time_planner(self):
        for algo in algorithms(time_planner):
            self.assertEqual([60, 68], algo([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
            self.assertEqual(None, algo([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))


if __name__ == '__main__':
    unittest.main()

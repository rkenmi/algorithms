import unittest

from heaps import merge_sorted_sequences
from utils import algorithms


class Heaps(unittest.TestCase):
    def test_merge_sorted_sequences(self):
        for algo in algorithms(merge_sorted_sequences):
            sequences = [
                [1, 3, 5],
                [2, 6],
                [1, 4, 4],
            ]
            self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], algo(sequences))

            sequences = [
                [-5, 20],
                [10, 12, 14],
                [5, 7, 15],
            ]
            self.assertEqual([-5, 5, 7, 10, 12, 14, 15, 20], algo(sequences))

            sequences = [
                [2, 2, 2],
                [2, 2],
                [2, 2, 2],
                [2, 2],
                [2, 2, 2],
                [2, 2],
                [2, 2, 2],
            ]
            self.assertEqual([2] * 18, algo(sequences))

            sequences = [
                [2],
                [],
                [3, 5],
                [1, 2, 3],
            ]
            self.assertEqual([1, 2, 2, 3, 3, 5], algo(sequences))

            sequences = [
                [0, 1, 2],
                [300, 310, 320],
                [99, 100, 101],
                [-100, -50, 0, 50, 100, 150]
            ]
            self.assertEqual([-100, -50, 0, 0, 1, 2, 50, 99, 100, 100, 101, 150, 300, 310, 320], algo(sequences))


if __name__ == '__main__':
    unittest.main()

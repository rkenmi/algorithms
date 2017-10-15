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
            """
            1st pass [-5, 5, 10]
            
            [-5, 5, 10, 20]
            out: -5 
            [5, 10, 20]
            [5, 10, 12, 20]
            
            out: -5, 5
            [10, 12, 20]
            [7, 10, 12, 20]
            
            out: -5, 5, 7
            [7, 12, 20]
            
            """
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


if __name__ == '__main__':
    unittest.main()

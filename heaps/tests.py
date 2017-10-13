import unittest

from heaps.merge_sorted_sequences import MergeSortedSequences


class Heaps(unittest.TestCase):
    def test_merge_sorted_sequences(self):
        mss = MergeSortedSequences()
        for algo in mss.get_functions():
            sequences = [
                [1, 3, 5],
                [2, 6],
                [1, 4, 4],
            ]
            self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], algo(sequences))

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
                [4, 2, 3],
                [5, 3, 0, 8],
            ]
            self.assertNotEqual([0, 2, 3, 3, 4, 5, 8], algo(sequences))

if __name__ == '__main__':
    unittest.main()

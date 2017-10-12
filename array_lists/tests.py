import unittest

from array_lists.longest_increasing_subsequence import longest_increasing_subsequence


class Lists(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        self.assertEquals(6, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))
        self.assertEquals(2, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))

if __name__ == '__main__':
    unittest.main()

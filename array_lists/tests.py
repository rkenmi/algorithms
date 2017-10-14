import unittest

from array_lists.longest_increasing_subsequence import longest_increasing_subsequence
from array_lists.next_greatest import NextGreatest


class Lists(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        self.assertEquals(6, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))
        self.assertEquals(2, longest_increasing_subsequence([-9, -4, 8, -2, 1, 4, -1, 3, 4]))

    def test_next_greatest(self):
        ng = NextGreatest()
        for algo in ng.get_functions():
            self.assertDictEqual({
                1: 9,
                3: 9,
                2: None,
                8: None,
                -5: 4,
                9: None,
                4: 8
            }, algo([3, 1, 9, -5, 4, 8, 2]))

            self.assertDictEqual({
                1: 5,
                -3: 9,
                5: 9,
                -4: 7,
                7: None,
                9: None
            }, algo([1, 5, -3, 9, -4, 7]))

            self.assertDictEqual({
                0: 1,
                1: 2,
                2: None
            }, algo([0, 1, 2]))

            self.assertDictEqual({
                0: None,
                1: None,
                2: None
            }, algo([2, 1, 0]))

if __name__ == '__main__':
    unittest.main()

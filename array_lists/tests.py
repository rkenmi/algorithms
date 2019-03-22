import unittest

# from array_lists import longest_increasing_subsequence
from array_lists import next_greatest, buy_and_sell_stock, longest_increasing_subsequence, buy_and_sell_stock_twice, \
    rotate_2d_array, min_in_rotated_sorted_array
from utils import algorithms

class Lists(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        for algo in algorithms(longest_increasing_subsequence):
            self.assertEqual(6, algo([-9, -4, 8, -2, 1, 4, -1, 3, 6]))

    def test_buy_sell_stocks(self):
        for algo in algorithms(buy_and_sell_stock):
            self.assertEqual(11, algo([6, 10, 8, 12, 4, 9, 10, 15]))
            self.assertEqual(4, algo([3, 4, 5, 7, 0]))
            self.assertEqual(2, algo([3, 4, 2, 4, 0]))
            self.assertEqual(0, algo([5, 4, 3, 2, 1]))
            self.assertEqual(0, algo([]))

    def test_min_in_rotated_sorted_array(self):
        for algo in algorithms(min_in_rotated_sorted_array):
            self.assertEqual(0, algo([1, 2, 3, 4, 5]))
            self.assertEqual(1, algo([9, 2, 3, 4, 5]))
            self.assertEqual(2, algo([9, 10, 3, 4, 5]))
            self.assertEqual(3, algo([9, 10, 11, 4, 5]))
            self.assertEqual(4, algo([9, 10, 11, 12, 5]))

    def test_buy_sell_stocks_twice(self):
        for algo in algorithms(buy_and_sell_stock_twice):
            self.assertEqual(17, algo([6, 10, 8, 12, 4, 9, 10, 15]))
            self.assertEqual(9, algo([3, 8, 1, 4, 5, 2]))

    def test_rotate_2d_array(self):
        for algo in algorithms(rotate_2d_array):
            self.assertEqual(algo([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                             [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
            self.assertEqual(algo([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]),
                             [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])

    def test_next_greatest(self):
        for algo in algorithms(next_greatest):
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

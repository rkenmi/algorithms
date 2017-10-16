import unittest

# from array_lists import longest_increasing_subsequence
from array_lists import next_greatest, buy_and_sell_stock, longest_increasing_subsequence, buy_and_sell_stock_twice
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

    def test_buy_sell_stocks_twice(self):
        for algo in algorithms(buy_and_sell_stock_twice):
            self.assertEqual(17, algo([6, 10, 8, 12, 4, 9, 10, 15]))
            self.assertEqual(9, algo([3, 8, 1, 4, 5, 2]))

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

import unittest

from binary_operations.swap_bits import SwapBits


class BinaryOperations(unittest.TestCase):
    def test_swap_bits(self):
        sb = SwapBits()
        for algo in sb.get_functions():
            self.assertEqual(0, algo(0, 2, 1))
            self.assertEqual(8, algo(16, 4, 3))
            self.assertEqual(6, algo(6, 0, 3))
            self.assertEqual(17, algo(24, 0, 3))
            self.assertEqual(24, algo(24, 2, 2))
            self.assertEqual(1, algo(128, 7, 0))


if __name__ == '__main__':
    unittest.main()

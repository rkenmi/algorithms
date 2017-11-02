import unittest

from mathematical import encircular, count_sq_root
from utils import algorithms


class MathematicalTests(unittest.TestCase):
    def test_encircular(self):
        for algo in algorithms(encircular):
            self.assertEqual(True, algo(["G", "L"]))
            self.assertEqual(True, algo(["G", "L", "G", "L"]))
            self.assertEqual(False, algo(["G", "L", "G", "R"]))
            self.assertEqual(True, algo(["G", "L", "G", "R", "G", "L"]))
            self.assertEqual(True, algo(["G", "R"]))
            self.assertEqual(False, algo(["G"]))
            self.assertEqual(True, algo(["L"]))
            self.assertEqual(True, algo(["L", "R"]))


    def test_count_sq_root(self):
        for algo in algorithms(count_sq_root):
            self.assertEqual(2, algo(4, 10))
            self.assertEqual(2, algo(3, 9))
            self.assertEqual(4, algo(4, 25))
            self.assertEqual(3, algo(5, 26))
            self.assertEqual(0, algo(5, 8))
            self.assertEqual(1, algo(4, 8))
            self.assertEqual(2, algo(4, 15))
            self.assertEqual(9, algo(4, 100))
            self.assertEqual(30, algo(4, 1000))
            self.assertEqual(2235, algo(2, 5000000))
            self.assertEqual(3161, algo(2, 10000000))
            #  the slow algorithm struggles beyond here
            self.assertEqual(1732049, algo(2, 3000000000000))

if __name__ == '__main__':
    unittest.main()

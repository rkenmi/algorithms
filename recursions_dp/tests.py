import unittest

from recursions_dp import deletion_distance
from utils import algorithms


class Recursions(unittest.TestCase):
    def test_deletion_distance(self):
        for algo in algorithms(deletion_distance):
            self.assertEqual(0, algo("", ""))
            self.assertEqual(3, algo("hit", ""))
            self.assertEqual(4, algo("", "hear"))
            self.assertEqual(3, algo("heat", "hit"))
            self.assertEqual(2, algo("hot", "not"))
            self.assertEqual(9, algo("some", "thing"))
            self.assertEqual(1, algo("abc", "adbc"))
            self.assertEqual(0, algo("awesome", "awesome"))
            self.assertEqual(2, algo("ab", "ba"))

"""

Test Case #2
Input: "", "hit",Expected: 3,Actual: 3
Test Case #3
Input: "neat", "",Expected: 4,Actual: 4
Test Case #4
Input: "heat", "hit",Expected: 3,Actual: 3
Test Case #5
Input: "hot", "not",Expected: 2,Actual: 2
Test Case #6
Input: "some", "thing",Expected: 9,Actual: 9
Test Case #7
Input: "abc", "adbc",Expected: 1,Actual: 1
Test Case #8
Input: "awesome", "awesome",Expected: 0,Actual: 0
Test Case #9
Input: "ab", "ba",Expected: 2,Actual: 2
"""
if __name__ == '__main__':
    unittest.main()
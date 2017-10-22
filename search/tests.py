import io
import unittest

from search import binary_search_first, int_sq_root, search_2d, kth_number, find_missing_ip
from search import binary_search_cyclic
from utils import algorithms


class BinarySearch(unittest.TestCase):
    def test_binary_search_first_occurence(self):
        for algo in algorithms(binary_search_first):
            self.assertEqual(0, algo([0, 1, 2], 0))
            self.assertEqual(2, algo([0, 1, 2], 2))
            self.assertEqual(5, algo([0, 1, 2, 3, 4, 5, 5, 6, 7], 5))
            self.assertEqual(0, algo([5, 5, 5, 5, 5, 5, 5], 5))
            self.assertEqual(-1, algo([5, 5, 5, 5, 5, 5, 5], 8))

    def test_binary_search_sorted_cyclic_array(self):
        for algo in algorithms(binary_search_cyclic):
            self.assertEqual(1, algo([3, 0, 1, 2]))
            self.assertEqual(3, algo([0, 1, 2, -1]))
            self.assertEqual(5, algo([4, 5, 6, 7, 8, 1, 2, 3]))
            self.assertEqual(0, algo([8, 9, 10]))
            self.assertEqual(-1, algo([]))

    def test_int_sq_root(self):
        for algo in algorithms(int_sq_root):
            self.assertEqual(5, algo(25))
            self.assertEqual(4, algo(24))
            self.assertEqual(4, algo(23))
            self.assertEqual(4, algo(17))
            self.assertEqual(4, algo(16))
            self.assertEqual(3, algo(15))
            self.assertEqual(9, algo(99))
            self.assertEqual(10, algo(100))

    def test_search_2d_matrix(self):
        matrix = [
            list(range(0, 5)),
            list(range(5, 10)),
            list(range(10, 15)),
            list(range(15, 20)),
            list(range(20, 25)),
        ]
        for algo in algorithms(search_2d):
            self.assertEqual(True, algo(matrix, 24))
            self.assertEqual(False, algo(matrix, -1))
            self.assertEqual(True, algo(matrix, 3))
            self.assertEqual(True, algo(matrix, 0))
            self.assertEqual(False, algo(matrix, 25))

class GeneralSearch(unittest.TestCase):
    def test_kth_largest_number(self):
        numbers = [9, 3, 5, 1, 7, 6]
        for algo in algorithms(kth_number):
            self.assertEqual(7, algo(numbers, 2))
            self.assertEqual(6, algo(numbers, 3))
            self.assertEqual(9, algo(numbers, 1))
            self.assertEqual(5, algo(numbers, 4))
            self.assertEqual(1, algo(numbers, 6))
            self.assertEqual(3, algo(numbers, 5))

        numbers = []
        for algo in algorithms(kth_number):
            self.assertRaises(IndexError, algo, numbers, 2)

        numbers = [8]
        for algo in algorithms(kth_number):
            self.assertRaises(ValueError, algo, numbers, 2)

    def test_search_missing_ip(self):
        fileobj = open("ip_addresses.txt")
        filelist = fileobj.read().splitlines()
        fileobj.close()
        filelist = map(self.ip_to_decimal, filelist)

        # ifs = input file stream using StringIO
        ifs = io.StringIO("\n".join(map(str, filelist)))

        for algo in algorithms(find_missing_ip):
            missing_ip = algo(ifs)
            self.assertEqual(self.ip_to_decimal('0.0.0.3'), missing_ip)


        ifs = io.StringIO("\n".join([str(i) for i in range(0, 2**18-100)]))
        for algo in algorithms(find_missing_ip):
            missing_ip = algo(ifs)
            self.assertEqual(self.ip_to_decimal('0.3.255.156'), missing_ip)


    def ip_to_decimal(self, ip):
        return int.from_bytes(bytes(map(int, ip.split("."))), "big")

    # def decimal_to_ip(self, dec):
    #     return bytes(dec)




if __name__ == '__main__':
    unittest.main()

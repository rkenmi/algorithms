import unittest

from linked_lists import merge_two_sorted_lists
from linked_lists.ListNode import ListNode
from utils import algorithms

class LinkedListTests(unittest.TestCase):
    def test_merge_sorted_lists(self):
        for algo in algorithms(merge_two_sorted_lists):
            L1 = ListNode(5)
            L1.next = ListNode(6)
            L1.next.next = ListNode(9)

            L2 = ListNode(1)
            L2.next = ListNode(2)
            L2.next.next = ListNode(8)

            sorted_merged_list = ListNode(1)
            sorted_merged_list.next = ListNode(2)
            sorted_merged_list.next.next = ListNode(5)
            sorted_merged_list.next.next.next = ListNode(6)
            sorted_merged_list.next.next.next.next = ListNode(8)
            sorted_merged_list.next.next.next.next.next = ListNode(9)

            L3 = algo(L1, L2)
            self.assertTrue(sorted_merged_list == L3)

if __name__ == '__main__':
    unittest.main()

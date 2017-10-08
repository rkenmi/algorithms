class ListNode(object):
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


    def print_all(self):
        temp = self
        to_print = []

        while temp:
            to_print.append(str(temp.data))
            temp = temp.next

        print(" => ".join(to_print))

sample = ListNode()
sample.next = ListNode(1)
sample.next.next = ListNode(2)
sample.next.next.next = ListNode(3)
sample.next.next.next.next = ListNode(4)
sample.next.next.next.next.next = ListNode(5)

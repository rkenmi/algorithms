class CircularQueue:
    """
        Constant time enqueue (amortized)
        Constant time dequeue
    """
    def __init__(self, capacity=10):
        self.elements = [None] * capacity
        self.head = self.tail = self.num_elems = 0

    def _resize(self):
        new_container = self.elements[self.head:] + self.elements[:self.head]
        self.head, self.tail = 0, self.num_elems
        self.elements = new_container + ([None] * self.num_elems)


    def enqueue(self, x):
        if self.num_elems is len(self.elements):
            self._resize()

        self.elements[self.tail % len(self.elements)] = x
        self.tail += 1
        self.num_elems += 1

    def dequeue(self):
        if self.num_elems is 0:
            raise IndexError("Cannot dequeue from empty queue")

        x = self.elements[self.head % len(self.elements)]
        self.head += 1
        self.num_elems -= 1

        return x

    def size(self):
        return self.num_elems

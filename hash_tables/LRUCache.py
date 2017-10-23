"""
    Notes:
        - A dictionary's pop and a list's pop is named the same as a method, but very different.
            A dictionary's pop is a (amortized) constant time operation and takes an immutable key argument.
            A list's pop is generally not constant time, but linear time.
                Popping the last element is an exception to this due to under-the-hood optimizations.
                As an argument, it takes an *integer* key argument.
"""

import collections


class LRUCacheSlow:

    def __init__(self, capacity):
        self._d = {}
        self.lru_queue = collections.deque()
        self.capacity = capacity

    def put(self, key, val):
        if key in self._d:
            self.lru_queue.remove(key)  # slow
        elif key not in self._d:
            if len(self._d) >= self.capacity:
                lru_key = self.lru_queue.popleft()
                self._d.pop(lru_key)

            self._d[key] = val

        self.lru_queue.append(key)

    def get(self, key):
        if key in self._d:
            self.lru_queue.remove(key)  # slow
            self.lru_queue.append(key)
            return self._d[key]

    def delete(self, key):
        if key not in self._d:
            return False

        self.lru_queue.remove(key)  # slow
        return self._d.pop(key) is not None

Element = collections.namedtuple('Element', 'data, index')

class LRUCache:
    """
        The bottleneck is the `remove` operation in the queue, since it has to search the entire queue.
        If we have a linked list implementation of a queue,
        we can get a specific node and make it the new head or tail in constant time.

        In this class, the index is stored in the lru_queue as part of the value in the dictionary.
        Using del is faster since we will already have the index we want to delete at hand.

        One problem with this is that the indices will get outdated as we delete entries and add entries, since
        entries in the queue can move around. To get around this, we use a counter to keep track
        of new elements only, and this counter will be used as an offset so that we can access the correct index
        in the queue. Since this counter can keep growing until overflow, it will reset if it becomes too high.
        The reset involves resetting the counter to 0 and all the indices in the dictionary's values, costing O(n) time.
        Since this only occurs in 1/65535 inserts, the amortized time for `put` is still O(1).

    """
    MAX_COUNTER = 65535

    def __init__(self, capacity):
        self._d = {}
        self.lru_queue = collections.deque()
        self.capacity = capacity
        self.counter = 0

    def put(self, key, val):
        if key in self._d:
            elem = self._d[key]
            del self.lru_queue[elem.index - self.counter]
            self.lru_queue.append(key)
        elif key not in self._d:
            if len(self._d) >= self.capacity:
                lru_key = self.lru_queue.popleft()
                self._d.pop(lru_key)
                if self.counter < self.MAX_COUNTER:
                    self.counter += 1
                else:
                    self._reset_counter()

            self.lru_queue.append(key)
            self._d[key] = Element(val, self.counter + len(self.lru_queue) - 1)

    def get(self, key):
        if key in self._d:
            elem = self._d[key]
            del self.lru_queue[elem.index - self.counter]
            self.lru_queue.append(key)
            return elem.data

    def delete(self, key):
        if key not in self._d:
            return False

        elem = self._d.pop(key)
        del self.lru_queue[elem.index - self.counter]
        return elem.data is not None

    def _reset_counter(self):
        local_counter = 0
        for key in self.lru_queue:
            self._d[key] = Element(self._d[key].data, local_counter)
            local_counter += 1

        self.counter = 0


class LRUCacheFast:
    """
        Use OrderedDict to simplify logic
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self._d = collections.OrderedDict()

    def put(self, key, val):
        if key in self._d:
            old_val = self._d.pop(key)
            self._d[key] = old_val  #  keep old value but set it to Most-Recently-Used
        else:
            if len(self._d) >= self.capacity:
                self._d.popitem(last=False)  # pop in FIFO order, i.e. queue-like
            self._d[key] = val


    def get(self, key):
        if key in self._d:
            old_val = self._d.pop(key)
            self._d[key] = old_val  #  keep old value but set it to Most-Recently-Used
            return self._d[key]

        return None


    def delete(self, key):
        return self._d.pop(key) is not None if key in self._d else False


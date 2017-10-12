
class Stack:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, e):
        self._stack.append(e)
        if len(self._max_stack) is 0 or self._max_stack[-1] <= e:
            self._max_stack.append(e)

    def pop(self):
        e = self._stack.pop()
        if e is self._max_stack[-1]:
            self._max_stack.pop()

        return e

    def empty(self):
        return len(self._stack) is 0

    def max(self):
        return self._max_stack[-1]
class _Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def push(self, element):
        node = _Node(element)
        node.next = self._head
        self._head = node
        self._size += 1
        return

    def pop(self):
        if self.is_empty():
            return False
        self._head = self._head.next
        self._size -= 1
        return

    def top(self):
        if self.is_empty():
            return False
        return self._head.data

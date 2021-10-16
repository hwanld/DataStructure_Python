import sys


class ListQueue:
    """General queue implementation using a Python list."""

    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        assert not self.is_empty()
        return self._items.pop(0)

    def front(self):
        assert not self.is_empty()
        return self._items[0]

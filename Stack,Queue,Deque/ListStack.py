import sys
import docx
#from exceptions import Empty


class ListStack:
    """General stack implementation using a Python list at the end."""

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

    def push(self, item):
        """Push item at the end of the list _items"""
        self._items.append(item)

    def pop(self):
        """Pop items at the end of the list _items"""
        assert not self.is_empty()

        return self._items.pop()

    def top(self):
        """Probe at top"""
        assert not self.is_empty()

        return self._items[-1]


if __name__ == '__main__':
    S = ListStack()  # contents: [ ]
    S.push(5)  # contents: [5]
    S.push(3)  # contents: [5, 3]
    print(len(S))  # contents: [5, 3];    outputs 2
    print(S.pop())  # contents: [5];       outputs 3
    print(S.is_empty())  # contents: [5];       outputs False
    print(S.pop())  # contents: [ ];       outputs 5
    print(S.is_empty())  # contents: [ ];       outputs True
    S.push(7)  # contents: [7]
    S.push(9)  # contents: [7, 9]
    print(S.top())  # contents: [7, 9];    outputs 9
    S.push(4)  # contents: [7, 9, 4]
    print(len(S))  # contents: [7, 9, 4]; outputs 3
    print(S.pop())  # contents: [7, 9];    outputs 4
    S.push(6)  # contents: [7, 9, 6]
    S.push(8)  # contents: [7, 9, 6, 8]
    print(S.pop())  # contents: [7, 9, 6]; outputs 8
    S.pop()
    S.pop()
    S.pop()
    print(S)
#    try:
#        S.pop()
#    except Empty
#        print("Empty stack error:", sys.exc_info())

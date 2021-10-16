from SList import SList


class SListStack:
    """ General stack implementation using a Python list at the end. """

    def __init__(self):
        self._items = SList()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def is_empty(self):
        return self._items.is_empty()

    def push(self, item):
        self._items.insert_first(item)

    def pop(self):
        assert not self.is_empty()
        return self._items.delete_first()

    def top(self):
        assert not self.is_empty()
        return self._items.head()


if __name__ == '__main__':
    S = SListStack()  # contents: [ ]
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

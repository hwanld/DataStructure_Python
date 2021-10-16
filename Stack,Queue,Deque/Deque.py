from DList import DList


class Deque(DList):
    def __init__(self):
        super().__init__()

    def insert_front(self, item):
        return self.insert_first(item)

    def delete_front(self):
        return self.delete_node(self.header().next())

    def insert_rear(self, item):
        return self.insert_last(item)

    def delete_rear(self):
        return self.delete_node(self.trailer().prev())

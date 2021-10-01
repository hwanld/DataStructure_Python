from SList import SList
from DList import DList
from CList import CList


# 2.7
def merge_slists(x, y):
    """Merge two Slists x and y into a Slist z, where x, y, z stores sorted integers respectively"""
    z = SList()
    xHead = x.head()
    yHead = y.head()
    for i in range(len(x)):
        z.insert_last(xHead)
        xHead = xHead.next()
    for i in range(len(y)):
        z.insert_last(yHead)
        yHead = yHead.next()
    return z
    #raise NotImplementedError

# 2.9


def reverse_slist(x):
    """Revers the order of Slist x inplace"""
    x.reverse_recursively(x.head())
    #raise NotImplementedError


# 2.12
def find_slist_middle_node(x):
    if (x.is_empty()):
        return None
    fastNode = x.head()
    slowNode = x.head()
    while(fastNode is not None and fastNode.next() is not None):
        fastNode = fastNode.next().next()
        slowNode = slowNode.next()
    return slowNode
    """Find middle node of SList x in O(n) time. You cannot use len(x) or x._size."""
    #raise NotImplementedError


# Finding the middle node of the DList
def find_dlist_middle_node(x):
    """Find middle node of DList x in O(n) time. You cannot use len(x) or x._size."""
    if (x.is_empty()):
        return None
    fastNode = x.header()
    slowNode = x.header()
    while(fastNode is not None and fastNode.next() is not None):
        fastNode = fastNode.next().next()
        slowNode = slowNode.next()
    return slowNode
    #raise NotImplementedError


# Finding the middle node of the CList
def find_clist_middle_node(x):
    """Find middle node of CList x in O(n) time. You cannot use len(x) or x._size."""
    if (x.is_empty()):
        return None
    elif (x.first() is x.last()):
        return x.first()
    fastNode = x.first()
    slowNode = x.first()
    while(fastNode is not x.last() and fastNode.next() is not x.last()):
        fastNode = fastNode.next().next()
        slowNode = slowNode.next()
    if (fastNode is x.last()):
        return slowNode
    elif(fastNode.next() is x.last()):
        return slowNode.next()
    #raise NotImplementedError


if __name__ == "__main__":
    # for test 2.7
    x = SList()
    y = SList()
    for i in range(10):
        x.insert_last(i*2+1)
        y.insert_last(i*2)
    print(x)
    print(y)
    z = merge_slists(x, y)
    print(z)

    # for test 2.9
    x = SList()
    for i in range(10):
        x.insert_last(i*2)
    print(x)
    reverse_slist(x)
    print(x)

    # for test 2.12
    x = SList()
    y = DList()
    z = CList()
    for i in range(10):
        x.insert_last(i*2)
        y.insert_last(i*2)
        z.insert(i*2)

    print(x)
    m = find_slist_middle_node(x)
    print("Middle node is {}".format(m))

    print(y)
    m = find_dlist_middle_node(y)
    print("Middle node is {}".format(m))

    print(z)
    m = find_clist_middle_node(z)
    print("Middle node is {}".format(m))

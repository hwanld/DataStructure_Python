from HeapPriorityQueue import HeapPriorityQueue as Heap


def HuffmanCode(freq_table):
    """Generating Huffman code for input frequency table.
    Frequency table is the list of (alphabet, frequency) pairs.
    This code should return the last entry of heap in tihs homework."""

    # Setp 1: Create an empty heap
    heap = Heap()

    # Setp 2: Insert (key, val) pair into the heap, where key=frequency and val=alphabet
    for i in range(len(freq_table)):
        heap.insert(freq_table[i][1], freq_table[i][0])

    # Step 3: Until there is only one pair in the heap,
    #             - Execute remove_min twice
    #             - Create a new (sum of the two keys, concatenation of two values) pair
    #                 * Two values, provided val1 and val2, should be concatenated as "[val1] [val2]"
    #             - Insert the new pair into the heap
    while(len(heap) != 1):
        first = heap.remove_min()
        second = heap.remove_min()
        newKey = first[0]+second[0]
        newValue = "["+first[1]+"] ["+second[1]+"]"
        heap.insert(newKey, newValue)

    # Setp 4: Return the last entry of the heap
    return heap.min()


if __name__ == "__main__":
    s = "abracadabra"
    f = [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
    e = HuffmanCode(f)
    print(e)
    # I expect the result of this homework as
    # (11, '[a] [[r] [[b] [[c] [d]]]]')

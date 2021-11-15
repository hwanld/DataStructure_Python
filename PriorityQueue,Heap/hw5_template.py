from typing import List
from HeapPriorityQueue import HeapPriorityQueue as Heap
from BinaryTree2 import BinaryTree


def build_huffman_tree(freq_table):
    """Generating Huffman code tree for input frequency table.
    Frequency table is the dictionary of (alphabet, frequency) pairs.
    This code should return the last entry of heap in tihs homework."""

    # Setp 1: Create an empty heap
    h = Heap()

    # Setp 2: Insert all the (key, val) pairs in the frequency table into the heap,
    # where key=frequency and val=a binary tree whose root contains the alphabet
    for alphabet, frequency in freq_table:
        bt = BinaryTree()
        bt.add_root(alphabet)
        h.insert(frequency, bt)

    # Step 3: Until there is only one pair in the heap,
    #             - Execute remove_min twice
    #             - Create a new (sum of the two keys, concatenation of two binary trees) pair
    #                 * Two binary trees, bt1 and bt2, should be concatenated as [frequency [bt1] [bt2]]
    #             - Insert the new pair into the heap
    while len(h) > 1:
        (k1, v1) = h.remove_min()
        (k2, v2) = h.remove_min()
        key = k1 + k2
        bt = BinaryTree()
        bt.add_root(key)
        bt.attach(bt.root(), v1, v2)
        h.insert(key, bt)

    # Setp 4: Return the last entry of the heap
    return h.remove_min()


def generate_code(node, code_table, prefix=""):
    """Generate Huffman codes recursively from the node of Huffman code tree into code_table"""
    # If node has left, call recursively for the left subtree with '0'+prefix
    if node.left() is not None:
        generate_code(node.left(), code_table, prefix + '0')
    # If node has right, call recursively for the right subtree with '1'+prefix,
    if node.right() is not None:
        generate_code(node.right(), code_table, prefix + '1')
    # If node is external, append (alphabet, prefix) into the code_table."""
    if node.left() is None and node.right() is None:
        code_table.append((node.element(), prefix))


def gen_freq_table(s):
    """Generate and compute the frequency tables of the input s as a list of [alphabet, frequency]"""
    freq_table = []

    def is_in_freq(alpha):
        for i in range(len(freq_table)):
            if freq_table[i][0] is alpha:
                return i
        return None

    for i in range(len(s)):
        alpha = s[i]
        if is_in_freq(alpha) is None:
            new = [alpha, 1]
            freq_table.append(new)
        else:
            freq_table[is_in_freq(alpha)][1] += 1

    return freq_table


if __name__ == "__main__":
    # s = "aaaabbbbccccddddeeee"
    # I will test your code with
    s = "In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression."

    # f will be or looks like [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
    f = gen_freq_table(s)
    print(f)

    # t is a pair of (key, huffman code tree) for the frequency table f
    t = build_huffman_tree(f)
    print(t[1])  # print the huffman code tree only
    # Output looks like [11 [a] [6 [r] [4 [b] [2 [c] [d]]]]]

    # Now generate codes of alphabets according to the huffman code tree
    code_tbl = []
    generate_code(t[1].root(), code_tbl, "")
    # Output looks like [('a', '0'), ('r', '10'), ('b', '110'), ('c', '1110'), ('d', '1111')]
    print(code_tbl)

    # Compute how the input string s is encoded by code_tbl
    print(f"Input={s}, Size={len(s)} characters")
    print(f"Encoded=", end="")
    count = 0
    for c in s:
        for alphabet, code in code_tbl:
            if alphabet == c:
                print(code, end="")
                count += len(code)
                break
    print(f", Size={count} bits")
    print("Total gain with respect to ASCII: {}/{} = {:.2f}%".format(count,
          len(s)*8, count/(len(s)*8)*100))

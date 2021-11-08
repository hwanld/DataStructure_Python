1. PriorityQueue
2. HeapPriorityQueue



<h3>Assignment4</h3>

<b>1. Implement HuffmanCode </b>

-Generating Huffman code for input frequency table.
-Frequency table is the list of (alphabet, frequency) pairs.

-First, Create an empty heap.

-Second, Insert (key, value) pair from list to heap.

-Third, do operations while there is only one pair in the heap.<br>
-Execute remove_min twice, create a new pair and insert new pair into the heap.<br>
-New pair is the result of adding two result of remove_min.<br>
-Using + operation at the value string. Now it's easy to implement adding two values.<br>

-Finally, return the last entry of the heap.


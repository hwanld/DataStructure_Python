LinkedList<br>
1. SinglyLinkedList<br>
2. DoublyLinkedList<br>
3. CircularLinkedList<br>

<h3>Assignment2</h3>
<b>1. Merge two SinglyLinkedList and return sotred merged list</b><br>
-Because two input lists are sotred, it's easy to make merged list with sorted.<br>
-Make two node and insert both list's head.<br>
-Compare two node's value and push the node which has less value than the other.<br>
-Change the node to the next one which value is pushed.<br>
-Do this process until both two node is None.<br><br>
<b>2. Reverse SinglyLinkedList</b><br>
-Because the function is located at SList.py, just using the functions.<br><br>
<b>3. Find SinglyLinkedList middle node</b><br>
-Make two node;fastNode and slowNode.<br>
-For a count, set fastNode to the next of next Node.<br>
-Also, set slowNode to the next Node.<br>
-Do this process while the fastNode is None.<br>
-After that, return slowNode.<br><br>
<b>4. Find DoublyLinkedList middle node</b><br>
-This function has same process of SinglyListNode.<br>
-Be careful that there is not head at DoublyLinkedList; header and trailer.<br><br> 
<b>5. Find CircularlLinkedList middle node</b><br>
-Same as singly, doublyLinkedList but there is no None at there.<br>
-So if fastNode becomed the tail of CircularLinkedList or the node before the tail, return slowNode.<br>

1. Stack
2. Queue
3. Deque
 
<h3>Assignment3)</h3>
**1. Make Leaky Stack**
- The stack can't contain information which is more than the number of maxCap; maxCap is the limit capacity for stack.
- If the stack is pushed more than maxCap, it has to be poped the bottom value and push the new item.
- Using Deque, when push or pop, use insert_rear and delete_rear
- Also when pushing, always check if the capacity is overflowed. If it is overflowed, delete the bottom value with delete_first.
- Using return trailer.prev() to make top() method.
- Also always have to do exception check; with is_empty() <br>
**2. Make function;infix_expression_evaluation**
- The string exp is given like (14 + 2 * 3 - 5) and have to return the evaluated value.
- There are 2 ideas : concat with ' ' to find operand and operation or check if the next string value is also operand, calculate with +=*10^n
- Concat with ' ' is not a good idea because the input must be seperated by space.
- First, make 2 stack; valueStack (operandStack) and operatorStack
- Second, make prec(token) function to determine if it is operator or operand or nullspace. Also we can know the order of operators.
- If given exp[i] is operand, check the next value exp[i+1] is operand or not. Then calculate until the next index's value is not operand. After that, push to the valueStack.
- If given exp[i] is operator, check if the operatorStack is empty or not. If empty, push it. If not empty, compare the order of given operator with top() of operatorStack.
- Check the order and if it is needed, do operation with 2 values and operator ; using doOperation() function to make clean code.
- After doing operation, we have to check operatorStack one more time to compare the order of operations ; using reculsive calling.
- If the exp[i] is the end of exp string, push '$' operator which order is the lowest ; to get all the left value and operator.
- The final value;result we want to get is in the valueStack. Pop() and return.

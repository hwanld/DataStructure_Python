# Import everything you have to use
from Deque import Deque
from ListStack import ListStack


class LeakyStack:
    def __init__(self, maxCap=10):
        self._maxCap = maxCap
        self._items = Deque()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self)

    def is_empty(self):
        return self._items.is_empty()

    def push(self, item):
        if len(self._items) is self._maxCap:
            self._items.delete_front()
        return self._items.insert_rear(item)

    def pop(self):
        if self._items.is_empty is True:
            return None
        else:
            return self._items.delete_rear()

    def top(self):
        if self._items.is_empty is True:
            return None
        else:
            return self._items.trailer().prev()


def evaluate_infix_expression(exp):
    operatorStack = ListStack()
    valueStack = ListStack()
    i = 0
    while (i < len(exp)):
        if prec(exp[i]) == None:
            pass
        elif prec(exp[i]) == 0:
            insertValue = 0
            value = ListStack()
            value.push(exp[i])
            while i+1 < len(exp):
                if prec(exp[i+1]) != 0:
                    break
                i += 1
                value.push(exp[i])
            digit = 1
            while value.is_empty() is not True:
                insertValue += (int)(value.pop()) * digit
                digit *= 10
            valueStack.push(insertValue)
        else:
            doOperationWithGivenOperator(operatorStack, valueStack, exp[i])
        i += 1
    doOperationWithGivenOperator(operatorStack, valueStack, '$')
    return valueStack.pop()


def doOperationWithGivenOperator(operatorStack, valueStack, operator):
    if operatorStack.is_empty():
        operatorStack.push(operator)
    else:
        if prec(operatorStack.top()) < prec(operator):
            operatorStack.push(operator)
        else:
            a = (int)(valueStack.pop())
            b = (int)(valueStack.pop())
            valueStack.push(doOperation(b, a, operatorStack.pop()))
            doOperationWithGivenOperator(operatorStack, valueStack, operator)


def prec(token):
    if token == '+' or token == '-':
        return 1
    elif token == '*' or token == '/':
        return 2
    elif token == '$':
        return -1
    elif token == ' ':
        return None
    else:
        return 0


def doOperation(a, b, op):
    if op == '+':
        print("{} + {}".format(a, b))
        return a+b
    elif op == '-':
        print("{} - {}".format(a, b))
        return a-b
    elif op == '*':
        print("{} * {}".format(a, b))
        return a*b
    elif op == '/':
        print("{} / {}".format(a, b))
        return a/b


if __name__ == "__main__":
    # Test for LeakyStack
    address = LeakyStack(5)
    address.push(1)
    address.push(2)
    address.push(3)
    address.push(4)
    address.push(5)
    print(address)
    what = address.pop()
    print("Pop {} becomes {}".format(what, address))
    address.push(6)
    print(address)
    address.push(7)
    print("Top {} element at {}".format(address.top(), address))
    what = address.pop()
    print("{} is popped at {}".format(what, address))

    # Test for evaluation of infix expression
    exp = "14 - 3 * 2 + 7"
    print(f"Evaluation of \'{exp}\' is {evaluate_infix_expression(exp)}")

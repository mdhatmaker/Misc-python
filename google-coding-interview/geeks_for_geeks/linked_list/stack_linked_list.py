import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1


# You have a linked list and you have to implement the functionalities push and pop
# of stack using this given linked list.

###############################################################################

stack = LinkedList()

def push(x):
    n = Node(x)
    n.next = stack.root
    stack.root = n
    return

def pop():
    n = stack.root
    if n == None:
        return -1
    else:
        stack.root = n.next
        return n.data

def process_stack_commands(ll):
    stack.clear()
    n = ll.root
    values = LinkedList()
    while n != None:
        if n.data == 1:
            n = n.next
            push(n.data)
        elif n.data == 2:
            x = pop()
            values.append(x)
        n = n.next
    return values

###############################################################################

if __name__ == "__main__":

    # A Query Q is of 2 Types
    # (i)  1 x   (a query of this type means  pushing 'x' onto the stack)
    # (ii) 2     (a query of this type means to pop element from stack and print the popped element)

    test_inputs = []
    test_inputs.append( ("1 2 1 3 2 1 4 2", "3 4") )
    test_inputs.append( ("2 1 4 1 5 2", "-1 5") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{ll}')
        values = process_stack_commands(ll)
        print(f"{values} expected: {results}\n")


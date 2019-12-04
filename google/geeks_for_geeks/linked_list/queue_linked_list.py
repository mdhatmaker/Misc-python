import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1


# Implement a Queue using Linked List.

###############################################################################

q = LinkedList()

def enq(x):
    q.append(x)
    return

def deq():
    n = q.root
    if n == None:
        return -1
    else:
        q.root = n.next
        return n.data

def process_queue_commands(ll):
    q.clear()
    n = ll.root
    values = LinkedList()
    while n != None:
        if n.data == 1:
            n = n.next
            enq(n.data)
        elif n.data == 2:
            x = deq()
            values.append(x)
        n = n.next
    return values

###############################################################################

if __name__ == "__main__":

    # A Query Q is of 2 Types
    # (i)  1 x   (a query of this type means  pushing 'x' into the queue)
    # (ii) 2     (a query of this type means to pop element from queue and print the popped element)

    test_inputs = []
    test_inputs.append( ("1 2 1 3 2 1 4 2", "2 3") )
    test_inputs.append( ("1 2 2 2 1 3", "2 -1") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{ll}')
        values = process_queue_commands(ll)
        print(f"{values} expected: {results}\n")


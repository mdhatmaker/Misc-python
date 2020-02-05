import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1


# Given a singly linked list of size N. The task is to rotate the linked list
# counter-clockwise by k nodes, where k is a given positive integer smaller than
# or equal to length of the linked list.

###############################################################################

def rotate(ll, k):
    n = ll.root
    for i in range(k):
        if n.next == None:
            n = ll.root
        else:
            n = n.next
    start_node = n
    while n.next != start_node:
        if n.next == None:
            n.next = ll.root
        n = n.next
    n.next = None
    ll.root = start_node
    return ll

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, "1 2 3 4 5 6 7 8", "5 6 7 8 1 2 3 4") )
    test_inputs.append( (3, "2 4 7 8 9", "8 9 2 4 7") )
    test_inputs.append( (4, "1 2", "1 2") )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{k}, {ll}')
        rotate(ll, k)
        print(f"{ll} expected: {results}\n")


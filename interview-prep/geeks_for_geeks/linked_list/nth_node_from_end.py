import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

# Given a linked list consisting of L nodes and given a number N. The task is
# to find the Nth node from the end of the linked list.

###############################################################################

def kth_from_end(ll, k):
    rv = -1
    kth = None
    n = ll.root
    i = 0
    while n != None:
        i += 1
        if i >= k:
            if kth == None:
                kth = ll.root
            else:
                kth = kth.next
        n = n.next
    return kth.data if kth != None else -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, "1 2 3 4 5 6 7 8 9", 8) )
    test_inputs.append( (4, "10 20 30 40 50 60 70 80 90", 60) )
    test_inputs.append( (5, "10 7 100 7", -1) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{k}th from end, {ll}')
        x = kth_from_end(ll, k)
        print(f"{x} expected: {results}\n")


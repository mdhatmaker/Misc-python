import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1


# Given a singly linked list of size N. The task is to swap elements in the
# linked list pairwise.

###############################################################################

def pairwise_swap(ll):
    n1 = ll.root
    #ll.root = n1.next
    while n1 != None:
        n2 = n1.next
        next = n2.next
        #n1, n2 = n2, n1
        n1.next, n2.next = n2.next, n1.next
        n1 = next
    return ll

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 2 4 5 6 7 8", "2 1 4 2 6 5 8 7") )
    test_inputs.append( ("1 2", "2 1") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{ll}')
        pairwise_swap(ll)
        print(f"{ll} expected: {results}\n")


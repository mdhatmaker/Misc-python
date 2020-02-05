import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1


# Given a linked list of size N. The task is to reverse every k nodes (where k is
# an input to the function) in the linked list.

###############################################################################

def reverse_groups(ll, k):
    prev = next = None
    curr = ll.root
    i = 1
    while curr != None:
        next = curr.next
        if i % (k+1) != 0:
            curr.next = prev
        prev = curr
        curr = next
        i += 1
        #if i == k:
        #    make_root = curr
    ll.root = prev
    return ll

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, "1 2 2 4 5 6 7 8", "4 2 2 1 8 7 6 5") )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(k, ',', ll)
        reverse_groups(ll, k)
        print(f"{ll} expected: {results}\n")


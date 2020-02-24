import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1


# Given a linked list of N nodes where nodes can contain values 0s, 1s and 2s only.
# The task is to segregate 0s, 1s and 2s linked list such that all zeros segregate
# to headside, 2s at the end of the linked list and 1s in the mid of 0s and 2s.

###############################################################################

def sort_0s1s2s(ll):
    head0 = head1 = head2 = None
    prev0 = prev1 = prev2 = None
    n = ll.root
    while n != None:
        if n.data == 0:
            if head0 == None:
                head0 = n
            if prev0 != None:
                prev0.next = n
            prev0 = n
        elif n.data == 1:
            if head1 == None:
                head1 = n
            if prev1 != None:
                prev1.next = n
            prev1 = n
        else: #if n.data == 0:
            if head2 == None:
                head2 = n
            if prev2 != None:
                prev2.next = n
            prev2 = n
        n = n.next
    ll.root = head0
    prev0.next = head1
    prev1.next = head2
    prev2.next = None
    return ll

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 2 1 2 0 2 2", "0 1 1 2 2 2 2 2") )
    test_inputs.append( ("2 2 0 1", "0 1 2 2") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{ll}')
        sort_0s1s2s(ll)
        print(f"{ll} expected: {results}\n")


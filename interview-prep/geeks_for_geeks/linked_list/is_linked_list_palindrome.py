import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1


# Given a singly linked list of size N of integers. The task is to check if the
# given linked list is palindrome or not.

###############################################################################

def is_palindrome(ll):
    li1 = ll.to_list()
    prev = None
    n = ll.root
    while n != None:
        next = n.next
        n.next = prev
        prev = n
        n = next
    ll.root = prev
    li2 = ll.to_list()
    # compare orignal linked list to reversed linked list
    return li1 == li2

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 1", True) )
    test_inputs.append( ("1 2 3 4", False) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{ll}')
        tf = is_palindrome(ll)
        print(f"{tf} expected: {results}\n")


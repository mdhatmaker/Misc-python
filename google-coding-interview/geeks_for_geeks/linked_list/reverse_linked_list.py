import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1


# Given a linked list of N nodes. The task is to reverse this list.
#
# Input: Head of following linked list
# 1->2->3->4->NULL
# Output: Linked list should be changed to,
# 4->3->2->1->NULL
#
# Input: Head of following linked list
# 1->2->3->4->5->NULL
# Output: Linked list should be changed to,
# 5->4->3->2->1->NULL
#
# Input: NULL
# Output: NULL
#
# Input: 1->NULL
# Output: 1->NULL

###############################################################################

def reverse(ll):
    prev = next = None
    curr = ll.root
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    ll.root = prev
    return ll

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 4 5 6", "6 5 4 3 2 1") )
    test_inputs.append( ("2 7 8 9 10", "10 9 8 7 2") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(ll)
        reverse(ll)
        print(f"{ll} expected: {results}\n")


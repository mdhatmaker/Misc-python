import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1


# You are given a pointer/ reference to the node which is to be deleted from
# the linked list of N nodes. The task is to delete the node. Pointer/ reference
# to head node is not given. 
#
# Note: No head reference is given to you.

###############################################################################

def delete_without_head(n):
    # problems if n.next is None
    n.data = n.next.data
    n.next = n.next.next
    return

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (1, "1 2", "2") )
    test_inputs.append( (20, "10 20 4 30", "10 4 30") )

    """ Run process on sample inputs 
    """
    for x, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        print(f'{x}, {ll}')
        n = ll.root
        while n.data != x:
            n = n.next
        delete_without_head(n)
        print(f"{ll} expected: {results}\n")


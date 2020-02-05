import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

# Given a linked list of N nodes. The task is to check if the the linked list has
# a loop. Linked list can contain self loop.

###############################################################################

def contains_loop(ll):
    bag = {}
    n = ll.root
    while n != None:
        if n in bag:
            return True
        bag[n] = 1
        n = n.next
    return False

###############################################################################

if __name__ == "__main__":

    # tuple format: (recurse_to_this_index, list_values, correct_value)
    # (zero means do not recurse)
    test_inputs = []
    test_inputs.append( (2, "1 3 4", True) )
    test_inputs.append( (0, "1 8 3 4", False) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        ll = LinkedList(arr)
        tail = ll.tail()
        tail.next = ll.get_node(k-1)
        print(f'{k}, {arr}')
        tf = contains_loop(ll)
        print(f"{tf} expected: {results}\n")


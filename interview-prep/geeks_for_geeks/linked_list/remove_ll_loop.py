import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


# You are given a linked list of N nodes. The task is to remove the loop from
# the linked list, if present.

###############################################################################

def remove_loop(ll):
    bag = {}
    n = ll.root
    while n != None:
        bag[n] = 1
        if n.next in bag:
            n.next = None
            return True
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
        tf = remove_loop(ll)
        print(f"{tf} expected: {results}\n")

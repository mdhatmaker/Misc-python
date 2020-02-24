import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

# Given a Linked List of size N, where every node represents a linked list and
# contains two pointers of its type:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
#
# You have to flatten the linked list to a single linked list which should be sorted.
#       5 -> 10 -> 19 -> 28
#       |    |     |     |
#       V    V     V     V
#       7    20    22    35
#       |          |     |
#       V          V     V
#       8          50    40
#       |                |
#       V                V
#       30               45
#
# And after flattening the above list, the sorted linked list looks like:
#
# 5-> 7-> 8- > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50.
#
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.

###############################################################################

def flatten(ll):
    n = ll.root
    llret = LinkedList(n)
    r = n.data.root
    c = 
    while r != None:

        r = r.next
    return ll #llret

# ll1 -> number of elements in each sub-linked-list (including head)
# ll2 -> elements to be inserted into lists
def create_list(ll1, ll2):
    llret = LinkedList()
    n1 = ll1.root
    n2 = ll2.root
    while n1 != None:
        count = n1.data
        sublist = LinkedList()
        for i in range(count):
            sublist.append(n2.data)
            n2 = n2.next
        llret.append(sublist)
        n1 = n1.next
    return llret


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 2 3 4", "5 7 8 30 10 20 19 22 50 28 35 40 45", "5 7 8 10 19 20 22 28 30 35 40 45 50") )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        ll1 = LinkedList(arr1)
        ll2 = LinkedList(arr2)
        ll = create_list(ll1, ll2)  # create linked list with sub-linked-lists
        print(f'{ll1}, {ll2}')
        flat = flatten(ll)
        print(f"{flat} expected: {results}\n")


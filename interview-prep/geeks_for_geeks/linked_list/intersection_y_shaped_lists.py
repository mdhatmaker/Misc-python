import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/


# There are two singly linked lists of size N and M in a system. But, due to some
# programming error the end node of one of the linked list got linked into one of
# the node of second list, forming a inverted Y shaped list. Write a program to get
# the point where two linked lists intersect each other.

###############################################################################

def find_intersection(ll1, ll2):
    bag = {}
    n1 = ll1.root
    n2 = ll2.root
    while n1 != None or n2 != None:
        #print(bag)
        if n1 != None:
            if n1 in bag:
                return n1
            bag[n1] = 1
            n1 = n1.next
        if n2 != None:
            if n2 in bag:
                return n2
            bag[n2] = 1
            n2 = n2.next
    return None

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("10 20", "30 40 50", "5 10", 5) )
    test_inputs.append( ("10 20 30", "40 50", "10 20", 10) )
    test_inputs.append( ("10 20 30", "40 50 60", "7 8 9", 7) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, inputs3, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        arr3 = [int(s) for s in inputs3.split()]
        ll1 = LinkedList(arr1 + arr3)
        ll2 = LinkedList(arr2 + arr3)
        print(ll1, '\n', ll2)
        intersect = find_intersection(ll1, ll2)
        print(f"{intersect} expected: {results}\n")


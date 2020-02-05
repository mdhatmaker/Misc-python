import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1


# Given two sorted linked lists consisting of N and M nodes respectively. The task
# is to merge both of the list (in-place) and return head of the merged list.
#
# Note: It is strongly recommended to do merging in-place using O(1) extra space.

###############################################################################

def merge_linked(ll1, ll2):
    n1 = ll1.root
    n2 = ll2.root
    # we should check if either linked list is null and handle it here
    prev = None
    while n1 != None and n2 != None:
        if n1.data <= n2.data:
            if prev != None:
                prev.next = n1
            prev = n1
            n1 = n1.next
        else: #n2.data <= n1.data
            if prev != None:
                prev.next = n2
            prev = n2
            n2 = n2.next
    if n1 == None:
        prev.next = n2
    else:
        prev.next = n1
    return ll1 if ll1.root.data <= ll2.root.data else ll2

# This function will NOT optimize for extra space (it will create a linked list for results)
def merge_linked_slow(ll1, ll2):
    n1 = ll1.root
    n2 = ll2.root
    llret = LinkedList()
    while n1 != None or n2 != None:
        if n1 == None:
            llret.append(n2.data)
            n2 = n2.next
        elif n2 == None:
            llret.append(n1.data)
            n1 = n1.next
        elif n1.data <= n2.data:
            llret.append(n1.data)
            n1 = n1.next
        else: #n2.data <= n1.data
            llret.append(n2.data)
            n2 = n2.next
    return llret

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("5 10 15 40", "2 3 20", "2 3 5 10 15 20 40") )
    test_inputs.append( ("1 1", "2 4", "1 1 2 4") )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        ll1 = LinkedList(arr1)
        ll2 = LinkedList(arr2)
        print(f'{ll1}, {ll2}')
        #merged = merge_linked_slow(ll1, ll2)
        #print(f"{merged} expected: {results}\n")
        merged = merge_linked(ll1, ll2)
        print(f"{merged} expected: {results}\n")

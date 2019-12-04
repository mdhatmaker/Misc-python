import sys
from LinkedList import LinkedList, Node

# https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1


# Given two numbers represented by two linked lists of size N and M. The task is to
# return a sum list. The sum list which is a linked list representation of addition
# of two input numbers.

###############################################################################

def numeric_value(ll, n):
    return

def add_numeric(ll1, ll2):
    n1 = ll1.root
    n2 = ll2.root
    rv = LinkedList()
    carry = 0
    while n1 != None or n2 != None:
        if n1 == None:
            value = n2.data + carry
            rv.append(value % 10)
            carry = int(value / 10)
            n2 = n2.next
        elif n2 == None:
            value = n1.data + carry
            rv.append(value % 10)
            carry = int(value / 10)
            n1 = n1.next
        else:
            value = n1.data + n2.data + carry
            rv.append(value % 10)
            carry = int(value / 10)
            n1 = n1.next
            n2 = n2.next
    if carry != 0:
        rv.append(carry)
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 5", "3 4 5", "0 9 3") )
    test_inputs.append( ("6 3", "7", "0 7") )
    test_inputs.append( ("6 3", "7 7", "0 4 1") )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        arr1.reverse()
        arr2.reverse()
        ll1 = LinkedList(arr1)
        ll2 = LinkedList(arr2)
        print(f'{ll1}, {ll2}')
        summed = add_numeric(ll1, ll2)
        print(f"{summed} expected: {results}\n")


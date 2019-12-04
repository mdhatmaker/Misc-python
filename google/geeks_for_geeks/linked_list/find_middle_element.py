import sys

# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1


# Given a singly linked list of N nodes. The task is to find middle of the linked list.
# For example, if given linked list is 1->2->3->4->5 then output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print
# second middle element. For example, if given linked list is 1->2->3->4->5->6 then
# output should be 4.

def middle_element(ll):
    rv = 0
    
    return rv


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 4 5", 3) )
    test_inputs.append( ("2 4 6 7 5 1", 7) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        middle = middle_element(arr)
        print(f"{middle} expected: {results}\n")


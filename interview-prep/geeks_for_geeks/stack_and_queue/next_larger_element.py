import sys

# https://practice.geeksforgeeks.org/problems/next-larger-element/0


# Given an array A of size N having distinct elements, the task is to find the
# next greater element for each element of the array in order of their appearance
# in the array. If no such element exists, output -1 

###############################################################################

stack = []

def push(x):
    stack.append(x)
    return

def pop():
    return stack.pop()

def next_larger(arr):
    rv = []
    for x in arr:
        pass
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 3 2 4", "3 4 4 -1") )
    test_inputs.append( ("4 3 2 1", "-1 -1 -1 -1") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        nl = next_larger(arr)
        print(f"{nl} expected: {results}\n")


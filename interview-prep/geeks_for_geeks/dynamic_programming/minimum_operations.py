import sys

# https://practice.geeksforgeeks.org/problems/find-optimum-operation/0


# You are given a number N. You have to find the number of operations required to
# reach N from 0. You have 2 operations available:
# 
# Double the number
# Add one to the number

###############################################################################

def min_operations(n):
    
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (8, 4) )
    test_inputs.append( (7, 5) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        minops = min_operations(n)
        print(f"{minops} expected: {results}\n")


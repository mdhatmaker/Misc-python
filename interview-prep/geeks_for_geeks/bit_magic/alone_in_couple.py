import sys

# https://practice.geeksforgeeks.org/problems/alone-in-couple/0
# https://wiki.python.org/moin/BitwiseOperators


# In a party everyone is in couple except one. People who are in couple have
# same numbers. Find out the person who is not in couple.

###############################################################################

def find_nopair(arr):
    xor = 0
    for x in arr:
        xor = xor ^ x       # use XOR to find the non-paired number in array
    return xor
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 2 1", 3) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        alone = find_nopair(arr)
        print(f"{alone} expected: {results}\n")


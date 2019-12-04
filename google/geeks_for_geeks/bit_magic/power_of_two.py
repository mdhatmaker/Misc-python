import sys

# https://practice.geeksforgeeks.org/problems/power-of-2/0
# https://wiki.python.org/moin/BitwiseOperators


# Given a positive integer N. The task is to check if N is a power of 2.
# That is N is 2^x for some x.

###############################################################################

def is_power_of_two(n):
    for i in range(32):
        mask = 1 << i
        if n == mask:
            return True
    return False

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (1, True) )
    test_inputs.append( (98, False) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        tf = is_power_of_two(n)
        print(f"{tf} expected: {results}\n")


import sys

# https://practice.geeksforgeeks.org/problems/series-gp/0

# Given the first 2 terms A and B of a Geometric Series. The task is to find
# the Nth term of the series.

###############################################################################

def nth_term(A, B, N):
    mult = B/A
    res = A
    for i in range(N-1):    # because we are starting AFTER the 2nd term
        res *= mult
    return res

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, 3, 1, 2) )
    test_inputs.append( (1, 2, 2, 2) )

    """ Run process on sample inputs 
    """
    for A, B, N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = nth_term(A, B, N)
        print(f"{rv} expected: {results}")
    


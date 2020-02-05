import sys

# https://practice.geeksforgeeks.org/problems/series-ap/0

# Given the first 2 terms A and B of an Arithmetic Series,
# tell the Nth term of the series. 

###############################################################################

def nth_term(A, B, N):
    diff = B-A
    res = B
    for i in range(N-2):    # because we are starting AFTER the 2nd term
        res += diff
    return res

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, 3, 4, 5) )
    test_inputs.append( (1, 2, 10, 10) )

    """ Run process on sample inputs 
    """
    for A, B, N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = nth_term(A, B, N)
        print(f"{rv} expected: {results}")
    


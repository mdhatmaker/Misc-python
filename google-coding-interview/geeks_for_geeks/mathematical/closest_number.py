import sys

# https://practice.geeksforgeeks.org/problems/closest-number/0

# Given non-zero two integers N and M. The problem is to find the number closest
# to N and divisible by M. If there are more than one such number, then output
# the one having maximum absolute value.

###############################################################################

def closest_number(N, M):
    for i in range(abs(N)):
        ok1 = (N-i) % M == 0
        ok2 = (N+i) % M == 0
        if ok1 and ok2:
            return N-i if abs(N-i) > abs(N+i) else N+i
        elif ok1:
            return N-i
        elif ok2:
            return N+i
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (13, 4, 12) )
    test_inputs.append( (-15, 6, -18) )

    """ Run process on sample inputs 
    """
    for N, M, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = closest_number(N, M)
        print(f"{rv} expected: {results}")
    


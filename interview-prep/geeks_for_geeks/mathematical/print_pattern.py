import sys

# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1


###############################################################################

def print_pattern(N):
    print('N =', N)
    n = N
    while n > 0:
        for i in range(N, 0, -1):
            for j in range(n):
                print(i, end=' ')
            
        print('$', end='')
        n -= 1
    print()
    return ''

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, "2 2 1 1 $2 1 $") )
    test_inputs.append( (3, "3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $") )

    """ Run process on sample inputs 
    """
    for N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = print_pattern(N)
        print(f"{rv} expected: {results}")
    


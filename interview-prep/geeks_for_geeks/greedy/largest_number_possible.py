import sys

# https://practice.geeksforgeeks.org/problems/largest-number-possible/0


# Given two numbers 'N' and 'S' , find the largest number that can be formed
# with 'N' digits and whose sum of digits should be equals to 'S'.

###############################################################################

def listval(n):
    sum = 0
    for d in n:
        sum *= 10
        sum += d
    return sum

# TODO: fix this
def next_lower_number(n):
    i = len(n)-1
    if n[i] > 0:
        n[i] -=1
    else:
        n[i] = 9
        n[i-1] -= 1

def largest_number(N, S):
    n = [9] * N
    while True:
        if sum(n) == S:
            break
        next_lower_number(n)

    return listval(n)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, 9, 90) )
    test_inputs.append( (3, 20, 992) )

    """ Run process on sample inputs 
    """
    for n, s, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n} {s}')
        rv = largest_number(n, s)
        print(f"{rv} expected: {results}")



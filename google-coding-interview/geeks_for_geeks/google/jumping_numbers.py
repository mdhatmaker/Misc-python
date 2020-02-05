import sys


# https://practice.geeksforgeeks.org/problems/jumping-numbers/0

# Given a positive number X. Find all Jumping Numbers smaller than or equal to X. 
# Jumping Number: A number is called Jumping Number if all adjacent digits in it
# differ by only 1. All single digit numbers are considered as Jumping Numbers.
# For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

###############################################################################

def is_jumping(X):
    s = str(X)
    for i in range(len(s)-1):
        d1 = int(s[i])
        d2 = int(s[i+1])
        if abs(d2-d1) != 1:
            return False
    return True

def jumping(X):
    res = []
    for i in range(X+1):
        if is_jumping(i):
            print(i, end=' ')
            res.append(i)
    print()
    return

#1 0 2
#2 1 3
#3 2 4
def jumping2(X):
    for i in range(10):
        if X < i: break
        print(i, end=' ')
    for d0 in range(1, 10):
        d1 = d0-1
        d2 = d1+2
        n1 = d0 * 10 + d1
        n2 = d0 * 10 + d2
        if X < n1: break
        print(n1, end=' ')
        if X < n2: break
        print(n2, end=' ')
    print()
    return -1

###############################################################################

if __name__ == "__main__":

    # Output: All the jumping numbers less than X in sorted order.
    test_inputs = []
    test_inputs.append( (10, "0 1 2 3 4 5 6 7 8 9 10") )
    test_inputs.append( (50, "0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45") )
    #test_inputs.append( (150, "0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45") )

    """ Run process on sample inputs 
    """
    for X, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{X}')
        rv = jumping2(X)
        print(f"{rv} expected: {results}")


import sys

# https://practice.geeksforgeeks.org/problems/last-index-of-1/0


# Given a string S consisting only '0's and '1's,  print the last index of
# the '1' present in it.

def last_index(s):
    i = len(s)-1
    while i >= 0:
        if s[i] == '1':
            return i
        i -= 1
    return -1


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("00001", 4) )
    test_inputs.append( ("0", -1) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(inputs)
        ix = last_index(inputs)
        print(f"{ix} expected: {results}\n")


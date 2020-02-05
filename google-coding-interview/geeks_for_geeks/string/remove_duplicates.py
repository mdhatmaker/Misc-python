import sys

# https://practice.geeksforgeeks.org/problems/remove-duplicates/0


# Given a string, the task is to remove duplicates from it. Expected time
# complexity O(n) where n is length of input string and extra space O(1) under
# the assumption that there are total 256 possible characters in a string.
#
# Note: that original order of characters must be kept same. 

def remove_duplicates(arr):
    rv = []
    seen = {}
    for ch in arr:
        if ch not in seen:
            seen[ch] = 1
            rv.append(ch)
    return ''.join(rv)


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("geeksforgeeks", "geksfor") )
    test_inputs.append( ("geeks for geeks", "geks for") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        nodupes = remove_duplicates(inputs)
        print(f"{nodupes} expected: {results}\n")


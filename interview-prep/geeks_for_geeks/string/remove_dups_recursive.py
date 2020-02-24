import sys

# https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0


# TODO: the 'norecurse' method works, but we need to implement this with recursion!!!

# Given a string s, recursively remove adjacent duplicate characters from the
# string s. The output string should not have any adjacent duplicates.


# Function to remove duplicate character sequences (result should have no repeating chars)
def remove_dups(s, ix=0):
    arr = []
    i1 = 0
    while i1 <= len(s)-1:
        if i1 >= len(s)-1 or s[i1] != s[i1+1]:
            arr.append(s[i1])
            i1 += 1
        else:
            ch = s[i1]
            i1 += 1
            while i1 < len(s) and s[i1] == ch:
                i1 += 1
    return ''.join(arr)

# Function to remove duplicate character sequences (any character that is a sequence of
# duplicates is removed)
def remove_dups_norecurse(s):
    arr = []
    i1 = 0
    while i1 <= len(s)-1:
        if i1 >= len(s)-1 or s[i1] != s[i1+1]:
            arr.append(s[i1])
            i1 += 1
        else:
            ch = s[i1]
            i1 += 1
            while i1 < len(s) and s[i1] == ch:
                i1 += 1
    return ''.join(arr)


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("geeksforgeek", "gksforgk") )
    test_inputs.append( ("acaaabbbacdddd", "acac") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        res = remove_dups_norecurse(inputs)
        print(f"{res} expected: {results}\n")


import sys

# https://practice.geeksforgeeks.org/problems/form-a-palindrome/0


# TODO: complete this exercise!!!

# Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
# For Example:
# ab: Number of insertions required is 1. bab or aba
# aa: Number of insertions required is 0. aa
# abcd: Number of insertions required is 3. dcbabcd

def chars_to_palindrome(arr):
    rv = 0
    
    return rv


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("abcd", 3) )
    test_inputs.append( ("abba", 0) )
    test_inputs.append( ("geeks", 3) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        n = chars_to_palindrome(inputs)
        print(f"{n} expected: {results}\n")



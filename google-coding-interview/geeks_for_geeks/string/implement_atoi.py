import sys

# https://practice.geeksforgeeks.org/problems/implement-atoi/1


# Your task  is to implement the function atoi. The function takes a string(str)
# as argument and converts it to an integer and returns it.

def my_atoi(s):
    rv = 0
    for i in range(len(s)):
        ch = s[len(s)-1-i]
        if ch < '0' or ch > '9':
            return -1
        digit = ord(ch) - ord('0')
        rv += digit * 10**i
    return rv


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("123", 123) )
    test_inputs.append( ("21a", -1) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        x = my_atoi(inputs)
        print(f"{x} expected: {results}\n")


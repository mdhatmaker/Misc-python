import sys

# https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array/0


# Given a array of N strings, find the longest common prefix among all strings
# present in the array.

def longest_common_prefix(arr):
    rv = ""
    i1 = 0
    while True:
        ch = arr[0][i1]
        for word in arr:
            if i1 >= len(word):
                return rv
            elif word[i1] != ch:
                return rv
        rv += ch
        i1 += 1
    return "-1"


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("geeksforgeeks geeks geek geezer", "gee") )
    test_inputs.append( ("apple ape april", "ap") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [s for s in inputs.split()]
        print(arr)
        longest = longest_common_prefix(arr)
        print(f"{longest} expected: {results}\n")


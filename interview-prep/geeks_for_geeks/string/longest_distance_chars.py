import sys

# https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0


# Given a string S, find length of the longest substring with all distinct characters.
# For example, for input "abca", the output is 3 as "abc" is the longest substring
# with all distinct characters.

def longest(s):
    rv = 0
    subtotal = 0
    seen = {}
    for ch in s:
        if ch in seen:
            subtotal = 0
            seen.clear()
        else:
            subtotal += 1
            rv = max(rv, subtotal)
            seen[ch] = 1
    return rv


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("abababcdefababcdab", 6) )
    test_inputs.append( ("geeksforgeeks", 7) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        n = longest(inputs)
        print(f"{n} expected: {results}\n")


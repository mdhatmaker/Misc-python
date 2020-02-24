import sys

# https://practice.geeksforgeeks.org/problems/anagram/0


# Given two strings a and b consisting of lowercase characters. The task is to check
# whether two given strings are anagram of each other or not. An anagram of a string
# string is another string that contains same characters, only the order of characters
# can be different. For example, “act” and “tac” are anagram of each other.

def is_anagram(s1, s2):
    if len(s1) != len(s2): return False
    arr1 = list(s1)
    arr1.sort()
    arr2 = list(s2)
    arr2.sort()
    return arr1 == arr2


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("geeksforgeeks", "forgeeksgeeks", True) )
    test_inputs.append( ("allergy", "allergic", False) )
    test_inputs.append( ("allergy", "allergi", False) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        print(inputs1, inputs2)
        tf = is_anagram(inputs1, inputs2)
        print(f"{tf} expected: {results}\n")


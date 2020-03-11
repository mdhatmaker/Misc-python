import sys

# https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0


# TODO: improve performance (maybe relying on properties of a triangle?)

# Given an array of integers, write a function that returns true if there is
# a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.

def pythagorean_triplets(arr):

    return False

def pythagorean_triplets_slow(arr):
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                a = arr[i]**2
                b = arr[j]**2
                c = arr[k]**2
                if a + b == c or a + c == b or b + c == a:
                    return True
    return False


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("3 2 4 6 5", True) )
    test_inputs.append( ("5 2 4 6 3", True) )
    test_inputs.append( ("2 7 1 6 5", False) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        exist = pythagorean_triplets_slow(arr)
        print(f"{exist} expected: {results}\n")


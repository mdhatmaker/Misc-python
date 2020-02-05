import sys


# https://practice.geeksforgeeks.org/problems/finding-the-numbers/0

# You are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers
# exist in pairs whereas the other two numbers occur exactly once and are distinct. You
# need to find the other two numbers and print them in ascending order.

###############################################################################

def find_numbers(arr):
    s = set()
    for x in arr:
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    return sorted(s)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 2 1 4", "3 4") )
    test_inputs.append( ("2 1 3 2", "1 3") )
    
    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{inputs}')
        rv = find_numbers(arr)
        print(f"{rv} expected: {results}")


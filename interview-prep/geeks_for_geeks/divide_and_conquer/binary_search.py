import sys

# https://practice.geeksforgeeks.org/problems/binary-search/1


# Given a sorted array A[](0 based index) and a key "k"  you need to complete
# the function bin_search to  determine the position of the key if the key
# is present in the array. If the key is not  present then you have to return -1.
# The arguments left and right denotes the left most index  and right most index
# of the array A[]. There are multiple test cases. For each test case, this function
# will be called individually.

###############################################################################

def binary_search(arr, k, l, r):
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if k < arr[mid]:
        return binary_search(arr, k, l, mid)
    elif k > arr[mid]:
        return binary_search(arr, k, mid+1, r)
    else: #k == arr[mid]:
        return mid

# Function to call the binary search functio with the correct left (l) and right (r) parameters
def search_for(arr, k):
    return binary_search(arr, k, 0, len(arr)-1)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, "1 2 3 4 5", 3) )
    test_inputs.append( (445, "11 22 33 44 55", -1) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{k}, {arr}')
        ix = search_for(arr, k)
        print(f"{ix} expected: {results}\n")


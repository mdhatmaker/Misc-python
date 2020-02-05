import sys

# https://www.techiedelight.com/find-pair-with-given-sum-array/

# Find pair with given sum in the array.

def find_pair_sum(arr, k):
    print(k, end='  ')
    arr.sort()
    low = 0
    high = len(arr)-1
    while (low < high):
        if arr[low] + arr[high] == k:
            return (arr[low], arr[high])
        if arr[low] + arr[high] < k:
            low += 1
        else:
            high -= 1
    return (-1, -1)

###############################################################################

if __name__ == "__main__":

    arr = [8, 7, 2, 5, 3, 1]

    print(arr)
    print(find_pair_sum(arr, 10))
    print(find_pair_sum(arr, 9))
    print(find_pair_sum(arr, 14))


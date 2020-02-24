import sys

# http://www.techiedelight.com/find-duplicate-element-limited-range-array/

# Given a limited range array of size n where array contains elements in
# range 1 to n-1 with one element repeating, find duplicate number.

# using xor :: O(n)  O(1) space
def find_duplicate(arr):
    print(arr)
    xor = 0
    for x in arr:
        xor ^= x
    return x

# using hashing :: O(n)  O(n) space

# using '-' sign :: O(n)  O(1) space
def find_duplicate2(arr):
    print(arr)
    for x in arr:
        xx = abs(x)
        if arr[xx] < 0:
            # restore array here (every value = abs())
            return xx
        else:
            arr[xx] = -arr[xx]
    return -1

###############################################################################

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 4]
    print(find_duplicate(arr))
    print(find_duplicate2(arr))

    arr = [1, 2, 3, 4, 2]
    print(find_duplicate(arr))
    print(find_duplicate2(arr))




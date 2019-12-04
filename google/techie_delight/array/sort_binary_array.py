import sys

# https://www.techiedelight.com/sort-binary-array-linear-time/

# Given a binary array, sort it in linear time and constant space.

def sort_binary_array(arr):
    print(arr)
    zero_count = 0
    for x in arr:
        if x == 0:
            zero_count += 1
    for i in range(len(arr)):
        if i < zero_count:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr



###############################################################################

if __name__ == "__main__":

    arr = [1, 0, 1, 1, 0, 0, 1, 0, 1]

    print(sort_binary_array(arr))
    



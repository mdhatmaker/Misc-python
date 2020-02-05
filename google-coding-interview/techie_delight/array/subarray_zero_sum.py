import sys

# https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
# https://www.techiedelight.com/find-sub-array-with-0-sum/

# TODO: fix zero_sum_subarrays()

# Check if subarray with zero sum exists or not.
# Print all sub-arrays with 0 sum.

def exists_zero_sum(arr):
    print(arr)
    sums = { 0:1 }
    sum_so_far = 0
    for x in arr:
        sum_so_far += x
        if sum_so_far in sums:
            #print(x, sum_so_far)
            return True
        sums[sum_so_far] = 1
    return False

# THIS ISN'T CORRECT
def zero_sum_subarrays(arr):
    print(arr)
    sums = { 0:[-1] }
    sum_so_far = 0
    for x in arr:
        sum_so_far += x
        if sum_so_far in sums:
            print(sums[sum_so_far], x)
            sums[sum_so_far].append(sum_so_far)
        sums[sum_so_far] = [sum_so_far]
    return sums

###############################################################################

if __name__ == "__main__":

    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    print(exists_zero_sum(arr))
    print(exists_zero_sum([3, 2, -4, 3, 1]))
    print(exists_zero_sum([3, 2, -4, 3, 2]))
    print(exists_zero_sum([3, 4, -6, 3, 1]))
    print()

    print(zero_sum_subarrays(arr))



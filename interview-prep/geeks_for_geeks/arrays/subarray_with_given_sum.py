import sys

# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0#ExpectOP


# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array
# which adds to a given number S.

def find_subarray(arr, S):
    for i in range(len(arr)-1):
        i1 = i2 = i
        sum = arr[i]

        # end loop if we exceed our target sum or i1/i2 are outside bounds
        while sum <= S and not (i1-1 <= 0 and i2+1 >= len(arr)):
            if sum == S:
                return (i1+1, i2+1) # results expected with 1-indexing vs 0-indexing
            
            if i1-1 <= 0:
                i2 += 1
                sum += arr[i2]
            elif i2+1 >= len(arr):
                i1 -= 1
                sum += arr[i1]
            elif arr[i1-1] <= arr[i2+1]:
                i1 -= 1
                sum += arr[i1]
            else:
                i2 += 1
                sum += arr[i2]
    return (0, 0)

if __name__ == "__main__":

    # list of tuples ([A], S, (i1,i2))
    test_inputs = [([1,2,3,7,5], 12, (2,4)), ([1,2,3,4,5,6,7,8,9,10], 15, (1,5))]
    test_inputs.append(([1,4,2,3,1,4,7], 44, (0,0)))
    test_inputs.append(([1,4,2,3,1,4,7], 10, (1,4)))

    for case in test_inputs:
        A, S, result = case
        i1, i2 = find_subarray(A, S)
        print(i1, i2, "  expected:", result[0], result[1])



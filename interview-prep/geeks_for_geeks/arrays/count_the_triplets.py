import sys

# https://practice.geeksforgeeks.org/problems/count-the-triplets/0


# TODO:
# improve performance (right now O(n^3)?)
# can we hash calculated values to improve performance?
# allow for other than triplets (i.e. 4 integers, 5 integers, etc.)
# test performance on very large data sets

# Given an array of distinct integers. The task is to count all the triplets such
# that sum of two elements equals the third element.

def count_triplets(arr):
    triplets = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                li = [arr[i], arr[j], arr[k]]   # did this to allow for future beyond triplets (4, 5, 6, ...)
                sum_all = sum(li)
                for x in li:
                    if x == (sum_all - x):
                        triplets.append(li)
    return len(triplets) if len(triplets) > 0 else -1



if __name__ == "__main__":
    test_inputs = []
    test_inputs.append( ( "1 5 3 2", 2) )
    test_inputs.append( ( "3 2 7", -1) )

    for case in test_inputs:
        numbers, result = case
        split = numbers.split()
        li = []
        for s in split:
            li.append(int(s))
        count = count_triplets(li)
        print(count, "  expected:", result)


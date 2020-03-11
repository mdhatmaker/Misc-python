import sys

# https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0


# TODO: is there a way to do this without sorting the array?

# Given an array A of positive integers of size N, where each value represents
# number of chocolates in a packet. Each packet can have variable number of chocolates.
# There are M students, the task is to distribute chocolate packets such that :
#    1. Each student gets one packet.
#    2. The difference between the number of chocolates given to the students
#       having packet with maximum chocolates and student having packet with
#       minimum chocolates is minimum.

# given array of packets and number of students
def minimum_difference(arr, n):
    sorted = merge_sort(arr)
    print(sorted)
    i1 = 0
    i2 = len(sorted) - 1
    while i2 - i1 >= n:
        print(i1, i2)
        if sorted[i1+1] - sorted[i1] > sorted[i2] - sorted[i2-1]:
            i1 += 1
        else:
            i2 -= 1
    print(i1, i2)
    return sorted[i2] - sorted[i1]


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    else:
        middle = int(len(arr) / 2)
        first_half = merge_sort(arr[0:middle])
        second_half = merge_sort(arr[middle:len(arr)])
        merged = merge(first_half, second_half)
        return merged

def merge(aa, ab):
    ia = 0
    ib = 0
    merged = []
    while ia < len(aa) or ib < len(ab):
        if ib >= len(ab):   #or aa[ia] <= ab[ib]):
            merged.append(aa[ia])
            ia+=1
        elif ia >= len(aa):
            merged.append(ab[ib])
            ib+=1
        elif aa[ia] <= ab[ib]:
            merged.append(aa[ia])
            ia+=1
        else: # if (ia >= len(aa) or ab[ib] <= aa[ia]))
            merged.append(ab[ib])
            ib+=1
    return merged


if __name__ == "__main__":

    # input tuples: (#_of_students, values_in_packets, correct_result)
    test_inputs = []
    test_inputs.append( (5, "3 4 1 9 56 7 9 12", 6) )
    test_inputs.append( (3, "7 3 2 4 9 12 56", 2) )

    """ Run process on sample inputs 
    """
    for nstudents, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(nstudents, arr)
        mindiff = minimum_difference(arr, nstudents)
        print(f"{mindiff} expected: {results}\n")


import sys
import random


# Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).

# TODO: check to see if in-place merge is actually executing in O((n+m) log(n+m)) time

# Note: Expected time complexity is O((n+m) log(n+m)).
# DO NOT use extra space.  We need to modify existing arrays as following.
# Input: arr1[] = {10};
#        arr2[] = {2, 3};
# Output: arr1[] = {2}
#         arr2[] = {3, 10}  
#
# Input: arr1[] = {1, 5, 9, 10, 15, 20};
#        arr2[] = {2, 3, 8, 13};
# Output: arr1[] = {1, 2, 3, 5, 8, 9}
#         arr2[] = {10, 13, 15, 20} 

def merge(arr1, arr2):
    i1 = i2 = 0
    while i1 < len(arr1) or i2 < len(arr2):
        #print(i1, i2, arr1, arr2)
        if i1 >= len(arr1):
            i2 += 1
            #break
        elif i2 >= len(arr2):
            i1 += 1
            #break
        elif arr1[i1] <= arr2[i2]:
            i1 += 1
        elif arr2[i2] < arr1[i1]:
            tmp = arr1[i1]              # swap arr1[i1], arr2[i2]
            arr1[i1] = arr2[i2]
            arr2[i2] = tmp
            i = i2
            if i >= len(arr2)-1 or arr2[i] <= arr2[i+1]:
                pass #i2 += 1
                #print("(sorting)")
            else:
                while i < len(arr2)-1 and arr2[i] > arr2[i+1]:
                    tmp = arr2[i]
                    arr2[i] = arr2[i+1]
                    arr2[i+1] = tmp
                    i += 1
        #print("    ", arr1, arr2)
        
    return

# This function will use O(m+n) extra space for the result array
def merge_slow(arr1, arr2):
    a = []
    i1 = i2 = 0
    while i1 < len(arr1) or i2 < len(arr2):
        if i1 >= len(arr1):
            a.append(arr2[i2])
            i2 += 1
        elif i2 >= len(arr2):
            a.append(arr1[i1])
            i1 += 1
        elif arr1[i1] == arr2[i2]:
            a.append(arr1[i1])
            a.append(arr2[i2])
            i1 += 1
            i2 += 1
        elif arr1[i1] < arr2[i2]:
            a.append(arr1[i1])
            i1 += 1
        elif arr2[i2] < arr1[i1]:
            a.append(arr2[i2])
            i2 += 1
        else:
            print("\n************ WHAT???? *************")
    return a

def results_match(merged, arr1, arr2):
    i1 = 0
    arr = arr1
    for x in merged:
        if arr[i1] != x:
            return False
        i1 += 1
        if arr == arr1 and i1 >= len(arr1):
            i1 = 0
            arr = arr2
    return True

def print_details(merged, arr1, arr2):
    #print("A1:", arr1)
    #print("A2:", arr2)
    print(merged)
    print("A1':", arr1)
    print("A2':", arr2)
    print()

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 3 5 7", "0 2 6 8 9") )
    test_inputs.append( ("10 12", "5 8 20") )
    test_inputs.append( ("1 5 9 10 15 20", "2 3 8 13") )
    test_inputs.append( ("10", "2 3") )
    test_inputs.append( ("10 11", "2 3") )
    test_inputs.append( ("10 11", "2 3 4") )

    """ Run process on sample inputs 
    """
    ix = 1
    for inputs1, inputs2 in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]

        merged = merge_slow(arr1, arr2)
        merge(arr1, arr2)

        if results_match(merged, arr1, arr2):
            print(ix, "OK")
        else:
            print("\n", ix, "ERROR")
            print_details(merged, arr1, arr2)
        ix += 1
    print()


    """ Generate random test cases (lists of random lengths of random numbers)
    """
    ntests = 1000
    MAX_ARR_LENGTH = 10
    for ix in range(1, ntests+1):
        size = random.randint(1, MAX_ARR_LENGTH)
        arr1 = [random.randint(1, MAX_ARR_LENGTH) for x in range(size)]
        size = random.randint(1, MAX_ARR_LENGTH)
        arr2 = [random.randint(1, MAX_ARR_LENGTH) for x in range(size)]
        arr1.sort()
        arr2.sort()
       
        merged = merge_slow(arr1, arr2)
        merge(arr1, arr2)

        if results_match(merged, arr1, arr2):
            print(ix, "OK  ", '\n' if ix % 10 == 0 else '', end='')
        else:
            print("\n", ix, "ERROR")
            print_details(merged, arr1, arr2)

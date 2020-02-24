
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

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left,right)
        if pivot > 1:
            quick_sort(arr, left, pivot-1)
        if pivot + 1 < right:
            quick_sort(arr, pivot+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    while (True):
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            if arr[left] == arr[right]: return right
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
        else:
            return right
    
def print_array(arr, title=""):
    #print()
    print(title)
    for i in arr:
        print(i, end = " ")
    print()



arr = [ 2, 5, -4, 11, 0, 18, 22, 67, 51, 6 ]
print_array(arr, "Original array :")
quick_sort(arr, 0, len(arr)-1)
print_array(arr, "Sorted array (quicksort):")

print("---")

arr = [ 2, 5, -4, 11, 0, 18, 22, 67, 51, 6 ]
print_array(arr, "Original array :")
arr = merge_sort(arr)
print_array(arr, "Sorted array (mergesort):")



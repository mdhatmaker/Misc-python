import sys
from collections import deque


# find largest in unordered list (iterate whole list - O(n))
def find_largest(arr):
    max = 0
    for x in arr:
        if x > max:
            max = x
    return max

def find_kth_largest(arr, kth):
    max_stack = []
    for x in arr:
        if len(max_stack) < kth:
            max_stack.append(x)
        elif x > max_stack[0]:
            max_stack.pop()
            max_stack.append(x)
    return max_stack

# search sorted list
def binary_search(arr, key):
    return

# search in sorted 2-dimensional array

# saddleback search (?)

# search min AND max in same iteration through unordered list (process one PAIR of numbers at a time)

if __name__ == "__main__":

    arr = [2, 4, 1, 12, 3, 8, 5, 9]
    print(arr)
    print(find_kth_largest(arr, 1))

    print("\nSTACK")
    stack = ["Amar", "Akbar", "Anthony"]
    stack.append("Ram")
    stack.append("Iqbal")
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)

    print("\nQUEUE")
    queue = deque(["Ram", "Tarun", "Asif", "John"])
    queue.append("Akbar") 
    queue.append("Birbal")
    print(queue)
    print(queue.popleft())
    print(queue.popleft())
    print(queue)




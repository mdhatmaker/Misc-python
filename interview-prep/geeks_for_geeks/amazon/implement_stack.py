import sys

# Implement a stack with push(), pop() and min() in O(1) time.

stack = []
stack_mins = []

def push(x):
    stack.append(x)
    if len(stack_mins) == 0 or stack_mins[-1] >= x:
        stack_mins.append(x)
    print('push:', x)

def pop():
    x = stack.pop()
    if stack_mins[-1] == x:
        stack_mins.pop()
    print('pop:', x)
    return x

def min():
    print('min:', stack_mins[-1])
    return stack_mins[-1]

if __name__ == "__main__":

    # assume unique numbers on stack are integers >= 0

    push(4)
    push(3)
    push(1)
    push(2)

    min()
    pop()
    min()
    pop()
    min()

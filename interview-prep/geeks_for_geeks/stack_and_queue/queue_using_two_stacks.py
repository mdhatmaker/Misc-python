import sys

# https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1


# Implement a Queue using 2 stacks s1 and s2.

###############################################################################

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def clear(self):
        self.stack.clear()


s1 = Stack()
s2 = Stack()

q = []

def enq(x):
    q.append(x)
    return

def deq():
    if len(q) == 0:
        return -1
    else:
        return q.pop(0)

def process_queue_commands(arr):
    s1.clear()
    s2.clear()
    q.clear()
    values = []
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            i += 1
            enq(arr[i])
        elif arr[i] == 2:
            x = deq()
            values.append(x)
        i += 1
    return values

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 1 3 2 1 4 2", "2 3") )
    test_inputs.append( ("1 2 2 2 1 4", "2 -1") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = process_queue_commands(arr)
        print(f"{rv} expected: {results}\n")


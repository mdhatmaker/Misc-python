class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def clear(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.q = []

    def enq(self, x):
        self.q.append(x)
        return

    def deq(self):
        if len(self.q) == 0:
            return None # or return -1?
        else:
            return self.q.pop(0)
    
    def clear(self):
        self.q.clear()

    def is_empty(self):
        return len(self.q) == 0

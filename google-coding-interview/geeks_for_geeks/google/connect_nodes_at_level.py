import sys
from collections import deque

# https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1

# Given a binary tree, connect the nodes that are at same level.
# Structure of the given Binary Tree node is like following.
#
# struct Node
# {
#       int data;
#       Node* left;
#       Node* right;
#       Node* nextRight;
# }
# Initially, all the nextRight pointers point to garbage values. Your function should
# set these pointers to point next right for each node.

###############################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

def bfs(node):
    q = deque()
    q.append((node, 0))
    while q:
        (n, level) = q.popleft()
        print(n.data, level)
        if n.left: q.append((n.left, level+1))
        if n.right: q.append((n.right, level+1))
    

###############################################################################

if __name__ == "__main__":

    r = Node(10)
    r.left = Node(3)
    r.right = Node(5)
    r.left.left = Node(4)
    r.left.right = Node(1)
    r.right.right = Node(2)

    bfs(r)

    sys.exit()

    # Output: All the jumping numbers less than X in sorted order.
    test_inputs = []
    test_inputs.append( (10, "0 1 2 3 4 5 6 7 8 9 10") )
    test_inputs.append( (50, "0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45") )
    #test_inputs.append( (150, "0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45") )

    """ Run process on sample inputs 
    """
    for X, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{X}')
        rv = jumping2(X)
        print(f"{rv} expected: {results}")


import sys
from collections import deque

# https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

# Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes
# in the BST that lie in the given range.
#
# The values smaller than root go to the left side
# The values greater and equal to the root go to the right side

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
    
def add_node(root, data):
    if not root:
        return Node(data)
    prev = n = root
    while n:
        prev = n
        if data < n.data:
            n = n.left
        else:
            n = n.right
    if data < prev.data:
        prev.left = Node(data)
    else:
        prev.right = Node(data)

def count_nodes_in_range(node, l, h):
    if node and node.data >= l and node.data <= h:
        return 1 + count_nodes_in_range(node.left, l, h) + count_nodes_in_range(node.right, l, h)
    else:
        return 0

def get_count_of_node(root, l, h):
    if root == None:
        return 0
    c = 0
    if root.data <= h and root.data >= l:
        c += 1
    c += get_count_of_node(root.left, l, h)
    c += get_count_of_node(root.right, l, h)
    return c

###############################################################################

if __name__ == "__main__":

    #10 5 50 1 40 100
    r = Node(10)
    add_node(r, 5)
    add_node(r, 50)
    add_node(r, 1)
    add_node(r, 40)
    add_node(r, 100)
    count = count_nodes_in_range(r, 5, 45)
    count = get_count_of_node(r, 5, 45)
    print(count)
    bfs(r)

    #5 6 7 4 3
    r = Node(5)
    add_node(r, 6)
    add_node(r, 7)
    add_node(r, 4)
    add_node(r, 3)
    count = count_nodes_in_range(r, 2, 8)
    print(count)
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


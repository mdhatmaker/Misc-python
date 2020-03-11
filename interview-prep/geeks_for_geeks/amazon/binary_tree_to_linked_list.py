import sys
from collections import deque

# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1

# TODO: traverse_inorder() displays nodes in correct order, but WE NEED TO CREATE DLL

# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
# The left and right pointers in nodes are to be used as previous and
# next pointers respectively in converted DLL.
# The order of nodes in DLL must be same as Inorder of the given Binary Tree.
# The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
#
#           10
#         /    \
#       12      15
#      /  \    /
#     25  30  36
#
# The above tree should be converted in-place to this DLL (doubly-linked-list):
# 25<->12<->30<->10<->36<->15

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        return

def traverse_levels(root_node):
    q = deque()
    if root_node: q.append((root_node, 0, 0))
    while len(q) > 0:
        n, hd, level = q.popleft()
        print(n.data, '  horiz_dist:', hd, '  level:', level)
        if n.left: q.append((n.left, hd-1, level+1)) 
        if n.right: q.append((n.right, hd+1, level+1)) 
    
def traverse_inorder(node):
    if not node: return
    traverse_inorder(node.left)
    print(node.data, end=' ')
    traverse_inorder(node.right)

if __name__ == "__main__":

    bt = Node(10)
    bt.left = Node(12)
    bt.left.left = Node(25)
    bt.left.right = Node(30)
    bt.right = Node(15)
    bt.right.left = Node(36)

    traverse_levels(bt)

    traverse_inorder(bt)

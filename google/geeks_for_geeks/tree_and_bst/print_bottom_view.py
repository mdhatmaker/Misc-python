import sys
from BinaryTree import BinaryNode, BinaryTree
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1


# Given a binary tree, print the bottom view from left to right.
# A node is included in bottom view if it can be seen when we look at the tree from bottom.
#
#                     20
#                   /    \
#                  8      22
#                /   \      \
#               5     3      25
#                    /  \      
#                  10    14
#
# For the above tree, the bottom view is 5 10 3 14 25.
# If there are multiple bottom-most nodes for a horizontal distance from root, then
# print the later one in level traversal. For example, in the below diagram, 3 and 4
# are both the bottommost nodes at horizontal distance 0, we need to print 4.
#
#                       20
#                    /      \
#                  8         22
#                /   \      /  \
#               5     3    4    25
#                    / \      
#                  10   14
#
# For the above tree the output should be 5 10 4 14 25.

###############################################################################

def traverse(node, hd = 0, hd_dict = {}):
    if not node: return
    #print(node.data, hd, end='  ')
    hd_dict[hd] = node
    traverse(node.left, hd-1, hd_dict)
    traverse(node.right, hd+1, hd_dict)
    return [n for n in hd_dict.values()]

def print_bottom_view(root_node):
    if not root_node: return
    #BinaryTree.print_bt(root_node)
    hds = traverse(root_node)
    print(hds)
    return

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 R 1 3 L", "3 1 2") )
    test_inputs.append( ("10 20 L 10 30 R 20 40 L 20 60 R", "40 20 60 30") )
    test_inputs.append( ("20 8 L 20 22 R 8 5 L 8 3 R 3 10 L 3 14 R 22 25 R", "5 10 3 14 25") )
    test_inputs.append( ("20 8 L 20 22 R 8 5 L 8 3 R 3 10 L 3 14 R 22 4 L 22 25 R", "5 10 4 14 25") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [s for s in inputs.split()]
        print(f'{inputs}')
        tree = BinaryTree.make_tree(inputs)
        print_bottom_view(tree)
        print(f" expected: {results}\n")


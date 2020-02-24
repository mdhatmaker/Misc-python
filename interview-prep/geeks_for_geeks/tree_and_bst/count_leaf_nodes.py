import sys
from BinaryTree import BinaryNode, BinaryTree
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1


# Given a binary tree, count leaves in it.
# For example, there are two leaves in below tree
#
#        1
#      /   \
#    10     39
#   /
#  5

###############################################################################

def count_leaves_helper(node, count = [0]):
    if node.left or node.right:
        if node.left:
            count_leaves_helper(node.left, count)
        if node.right:
            count_leaves_helper(node.right, count)
    else:
        count[0] += 1

def count_leaves(node):
    count = [0]
    count_leaves_helper(node, count)
    return count[0]

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 R 1 3 L", 2) )
    test_inputs.append( ("10 20 L 10 30 R 20 40 L 20 60 R", 3) )
    test_inputs.append( ("1 10 L 10 5 L 1 39 R", 2) )
    test_inputs.append( ("20 8 L 20 22 R 8 5 L 8 3 R 3 10 L 3 14 R 22 25 R", 4) )
    test_inputs.append( ("20 8 L 20 22 R 8 5 L 8 3 R 3 10 L 3 14 R 22 4 L 22 25 R", 5) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [s for s in inputs.split()]
        print(f'{inputs}')
        tree = BinaryTree.make_tree(inputs)
        count = count_leaves(tree)
        print(f"{count} expected: {results}\n")


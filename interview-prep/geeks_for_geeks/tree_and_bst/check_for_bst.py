import sys
from BinaryTree import BinaryNode, BinaryTree
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/check-for-bst/1


# Given a binary tree, return true if it is BST, else false. For example, the
# following tree is not BST, because 11 is in left subtree of 10. The task is to
# complete the function isBST() which takes one argument, root of Binary Tree.
#
#      10
#    /    \
#   7      39
#    \
#     11

###############################################################################

INT_MIN = -1000000000
INT_MAX = 1000000000

def check_bst(node, submin = INT_MAX, submax = INT_MIN):
    if node.left or node.right:
        submin = min(submin, node.data)
        submax = max(submax, node.data)
        #print(node.data, ' L:', node.left, ' R:', node.right, ' min:', submin, ' max:', submax)
        if node.left:
            return node.left.data < submin and check_bst(node.left, submin, submax)
        if node.right:
            return node.right.data > submax and check_bst(node.right, submin, submax)
    else:
        return True

def is_bst(root_node):
    if not root_node: return False
    return check_bst(root_node)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 R 1 3 L", False) )
    test_inputs.append( ("10 20 L 10 30 R 20 40 L 20 60 R", False) )
    test_inputs.append( ("2 1 L 2 3 R", True) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [s for s in inputs.split()]
        print(f'{inputs}')
        tree = BinaryTree.make_tree(inputs)
        tf = is_bst(tree)
        print(f"{tf} expected: {results}\n")


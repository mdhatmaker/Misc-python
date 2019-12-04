import sys
from BinaryTree import BinaryNode, BinaryTree
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1


# Given a Binary Search Tree and 2 nodes value n1 and n2, your task is to find the
# lowest common ancestor(LCA) of the two nodes.
# Note: Duplicates are not inserted in the BST.

###############################################################################

def get_path(bst_node, x):
    path = []
    n = bst_node
    while n != None:
        path.append(n)
        if x < n.data:
            n = n.left
        elif x > n.data:
            n = n.right
        else: #x == n.data
            break
    return path if n else []

def find_lca(root_node, x1, x2):
    path1 = get_path(root_node, x1)
    path2 = get_path(root_node, x2)
    #print(path1, ', ', path2)
    bag = {}
    common = None
    i1 = len(path1)-1
    i2 = len(path2)-1
    while i1 >= 0 or i2 >= 0:
        if i1 < 0:
            n2 = path2[i2]
            if n2 in bag:
                common = n2
                break
            bag[n2] = 1
        elif i2 < 0:
            n1 = path1[i1]
            if n1 in bag:
                common = n1
                break
            bag[n1] = 1
        else:
            n1 = path1[i1]
            n2 = path2[i2]
            if n1 == n2 or n1 in bag:
                common = n1
                break
            elif n2 in bag:
                common = n2
                break
            bag[n1] = 1
            bag[n2] = 1
        i1 -= 1
        i2 -= 1
    #print(bag)
    return common


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("5 4 6 3 7 8", "7 8", 7) )
    test_inputs.append( ("12 14 15 10 9 8", "8 15", 12) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr2 = [int(s) for s in inputs2.split()]
        print(f'{inputs1}, {inputs2}')
        root_node = BinaryTree.make_bst(inputs1)
        #BinaryTree.print_bt(root_node)
        lca = find_lca(root_node, arr2[0], arr2[1])
        print(f"{lca} expected: {results}\n")


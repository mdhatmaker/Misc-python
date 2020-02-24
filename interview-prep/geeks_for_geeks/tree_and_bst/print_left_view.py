import sys
from BinaryTree import BinaryNode, BinaryTree
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1


# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of
# nodes visible when tree is visited from Left side. The task is to complete the
# function leftView(), which accepts root of the tree as argument.
#
# Left view of following tree is 1 2 4 8.
#
#          1
#       /     \
#     2        3
#   /   \    /   \
#  4     5  6     7
#   \
#    8

###############################################################################

def level_traversal(node):
    rv = []
    q = Queue()
    if node != None: q.enq(node)
    while not q.is_empty():
        n = q.deq()
        rv.append(n.data)
        if n.left != None: q.enq(n.left)
        if n.right != None: q.enq(n.right)
    return rv

# Uses Stack object (no recursion)
def pre_order(node):
    stk = Stack()
    if node != None: stk.push(node)
    while not stk.is_empty():
        n = stk.pop()
        print(n.data, end=' ')
        if n.right != None: stk.push(n.right)
        if n.left != None: stk.push(n.left)
    print()
    return

# Uses recursion
def pre_order_recur(node):
    if node == None:
        return
    print(node.data, end=' ')
    pre_order_recur(node.left)
    pre_order_recur(node.right)
    return

# Uses two Stack objects (no recursion)
# 1. Push root to first stack.
# 2. Loop while first stack is not empty
#    2.1 Pop a node from first stack and push it to second stack
#    2.2 Push left and right children of the popped node to first stack
# 3. Print contents of second stack
def post_order(node):
    st1 = Stack()
    st2 = Stack()
    if node != None: st1.push(node)
    while not st1.is_empty():
        n = st1.pop()
        st2.push(n)
        if n.left != None: st1.push(n.left)
        if n.right != None: st1.push(n.right)
    while not st2.is_empty():
        n = st2.pop()
        print(n.data, end=' ')
    print()
    return

# For postorder recursion using ONE stack:
# 1.1 Create an empty stack
# 2.1 Do following while root is not NULL
#     a) Push root's right child and then root to stack.
#     b) Set root as root's left child.
# 2.2 Pop an item from stack and set it as root.
#     a) If the popped item has a right child and the right child 
#        is at top of stack, then remove the right child from stack,
#        push the root back and set root as root's right child.
#     b) Else print root's data and set root as NULL.
# 2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

# Uses recursion
def post_order_recur(node):
    if node == None:
        return
    post_order_recur(node.left)
    post_order_recur(node.right)
    print(node.data, end=' ')
    return

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(node.data, end=' ')
    in_order(node.right)
    return
    
def test_traversals():
    pre_order(n)
    pre_order_recur(n)
    post_order(n)
    post_order_recur(n)
    print(level_traversal(n))


def print_left_view(root_node):
    n = root_node
    while n:
        print(n.data, end=' ')
        if n.left:
            n = n.left
        else:
            n = n.right
    return
    


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 R 1 3 L", "1 3") )
    test_inputs.append( ("10 20 L 10 30 R 20 40 L 20 60 R", "10 20 40") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [s for s in inputs.split()]
        print(f'{inputs}')
        tree = BinaryTree.make_tree(inputs)
        print_left_view(tree)
        print(f" expected: {results}\n")


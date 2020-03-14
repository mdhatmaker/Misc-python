import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add(root, value):
    if root == None:
        return Node(value)
    if value < root.value:
        return add(root.left, value)
    else:
        return add(root.right, value)

def inorder(root):
    if root == None: return
    if root.left: inorder(root.left)
    print(root.value)
    if root.right: inorder(root.right)


if __name__ == "__main__":

    bt = add(None, 10)
    add(bt, 7)
    add(bt, 13)
    add(bt, 1)
    add(bt, 4)

    inorder(bt)

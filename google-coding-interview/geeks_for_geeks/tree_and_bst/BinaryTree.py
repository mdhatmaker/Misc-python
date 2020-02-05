from StackAndQueue import Queue

class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left if left == None else BinaryNode(left)
        self.right = right if right == None else BinaryNode(right)

    def __repr__(self):
        return str(self.data)
        
    def __eq__(self, other):
      return other and self.data == other.data and self.left == other.left and self.right == other.right

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.data, self.left, self.right))

class BinaryTree:
    #def __init__(self):

    # Create Binary Tree from string describing the tree like "1 2 R 1 3 L"
    @staticmethod
    def make_tree(s):
        tree = None
        nodes = {}
        split = s.split()
        for i in range(0, len(split), 3):
            x1 = int(split[i])
            x2 = int(split[i+1])
            lr = split[i+2]
            if x1 in nodes:
                n1 = nodes[x1]
            else:
                n1 = BinaryNode(x1)
                nodes[x1] = n1
                if tree == None: tree = n1
            if x2 in nodes:
                n2 = nodes[x2]
            else:
                n2 = BinaryNode(x2)
                nodes[x2] = n2
            if lr == 'R':
                n1.right = n2
            else: #lr == 'L':
                n1.left = n2
        return tree

    # Create a Binary Search Tree (BST) from a string of values like "5 4 6 3 7 8"
    @staticmethod
    def make_bst(s):
        tree = None
        split = s.split()
        for i in range(0, len(split)):
            x = int(split[i])
            n = BinaryTree.bst_insert(tree, x)
            if not tree: tree = n
        return tree

    # Insert into a Binary Search Tree (BST)
    @staticmethod
    def bst_insert(node, key):
        if node == None:
            return BinaryNode(key)  # create new node
        if key < node.data:
            node.left = BinaryTree.bst_insert(node.left, key)
        elif key > node.data:
            node.right = BinaryTree.bst_insert(node.right, key)
        return node     # return existing node

    # Print Binary Tree using Level Traversal (Breadth-First)
    @staticmethod
    def print_bt(node):
        q = Queue()
        if node: q.enq(node)
        while not q.is_empty():
            n = q.deq()
            print(n.data, end=' ')
            if n.left: q.enq(n.left)
            if n.right: q.enq(n.right)
        print()

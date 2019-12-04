import sys


# Node class (for binary tree)
class Node: 
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.left = None  # Initialize left leaf as null
        self.right = None # Initialize right leaf as null


# Binary Tree Class
class BinaryTree:
    # Function to initialize the BinaryTree object
    def __init__(self):  
        self.root = None
    
    def append(self, data_list):
        for data in data_list:
            self.add(data)
        return

    def add(self, data):
        if self.root == None:
            self.root = Node(data)
            #print("Root: ", data)
        else:
            n = self.root
            while True:
                if data < n.data:
                    if n.left is None:
                        n.left = Node(data)
                        #print(f"Left: ", data)
                        break
                    else:
                        n = n.left
                else:
                    if n.right is None:
                        n.right = Node(data)
                        #print(f"Right: ", data)
                        break
                    else:
                        n = n.right
        return

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # A utility function to insert a new node with the given key 
    def insert(self, root, key): 
        if root is None: 
            self.root = Node(key)
        else: 
            if root.data < key:
                if root.right is None: 
                    root.right = Node(key)
                else: 
                    self.insert(root.right, key) 
            else: 
                if root.left is None: 
                    root.left = Node(key) 
                else:
                    self.insert(root.left, key)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print("%d " % node.data, end='  ')
        self.inorder(node.right)
        
    def preorder(self, node):
        if node is None:
            return
        print("%d " % node.data, end='  ')
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print("%d " % node.data, end='  ')

    def reverse_inorder(self, node):
        if node is None:
            return
        self.reverse_inorder(node.right)
        print("%d " % node.data, end='  ')
        self.reverse_inorder(node.left)



def find(bt, find_data):
    node = bt.search(bt.root, find_data)
    print('search for ', find_data, '  -->  ', '(null)' if node is None else node.data)

if __name__ == "__main__":

    bt = BinaryTree()
    bt.add(8)
    bt.append([3, 10])
    bt.append([1, 6, 14])
    bt.append([4, 7, 13])

    bt.inorder(bt.root)
    print()
    bt.preorder(bt.root)
    print()
    bt.postorder(bt.root)
    print()
    bt.reverse_inorder(bt.root)
    print()

    find(bt, 11)
    find(bt, 14)

    # Reverse Inorder BST search can find nth-largest value

    bt = BinaryTree()
    bt.insert(bt.root, 50)
    bt.insert(bt.root, 30)
    bt.insert(bt.root, 20)
    bt.insert(bt.root, 40)
    bt.insert(bt.root, 70)
    bt.insert(bt.root, 60)
    bt.insert(bt.root, 80)
    bt.inorder(bt.root)

    




    

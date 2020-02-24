import sys
from collections import deque


###############################################################################
# Node (for linked list or binary tree)
class Node:
    def get_l(self):
        return self.prev
    def set_l(self, value):
        self.prev = value
    def get_r(self):
        return self.next
    def set_r(self, value):
        self.next = value
    l = property(get_l, set_l)
    r = property(get_r, set_r)

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        return

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        if not other: return False
        return self.data == other.data and self.prev == other.prev and self.next == other.next

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.data, self.prev, self.next))


class LinkedList:
    def __init__(self):
        self.root = None

    # get tail node of linked list
    def tail(self):
        n = self.root
        while n and n.next:
            n = n.next
        return n

    # append to linked list
    def append(self, data):
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            node = self.tail()
            nnext = Node(data)
            node.next = nnext
            nnext.prev = node
            return nnext

    # add each value in the specified list to linked list
    def append_list(self, data_list):
        for data in data_list:
            self.append(data)

    def print_list(self):
        n = self.root
        while n:
            print(n.data, end=' -> ')
            n = n.next
        print()

    # reverse a linked list in-place
    def reverse_inplace(self):
        prev = None
        curr = self.root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        #return prev
        self.root = prev


class BinaryTree:
    def __init__(self):
        self.root = None

    # find in binary tree
    def find(self, data):
        n = self.root
        while n:
            if data == n.data:
                return n
            elif data < n.data:
                n = n.prev
            elif data > n.data:
                n = n.next
        return None

    # find the path to a specified data node (returns deque of nodes)
    def find_path(self, data):
        q = deque()
        n = self.root
        while n:
            q.append(n)
            if data == n.data:
                return q
            elif data < n.data:
                n = n.prev
            elif data > n.data:
                n = n.next
        return None

    # shortest path between two nodes in the binary tree
    def path_between(self, data1, data2):
        path1 = self.find_path(data1)
        path2 = self.find_path(data2)
        if path1 and path2:
            path_nodes = []
            while path1:
                path_nodes.append(path1.pop())
            path2.popleft() # skip duplicate of LCA node
            while path2:
                path_nodes.append(path2.popleft())
            return path_nodes
        else:
            return None

    # Lowest Common Ancestor
    def get_lca(self, data1, data2):
        path1 = self.find_path(data1)
        path2 = self.find_path(data2)
        bag = {}
        while path1 or path2:
            if path1:
                n1 = path1.pop()
                if n1 in bag:
                    return n1
                bag[n1] = 1
            if path2:
                n2 = path2.pop()
                if n2 in bag:
                    return n2
                bag[n2] = 1
        return None

    # add to binary tree
    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        n = self.root
        while True:
            if data < n.data:
                if not n.prev:
                    n.prev = Node(data)
                    return n.prev
                else:
                    n = n.prev
            elif data > n.data:
                if not n.next:
                    n.next = Node(data)
                    return n.next
                else:
                    n = n.next

    # add each value in the specified list to binary tree
    def add_list(self, data_list):
        for data in data_list:
            self.add(data)

    def print_tree(self):
        if not self.root: return
        q = deque()
        q.append(self.root)
        while q:
            n = q.popleft()
            print(n.data, end=' ')
            if n.prev: q.append(n.prev)
            if n.next: q.append(n.next)
        print()

 
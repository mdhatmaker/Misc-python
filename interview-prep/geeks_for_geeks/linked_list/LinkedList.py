class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return other and self.data == other.data and self.next == other.next

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        #return hash((self.a, self.b))
        #return hash((self.data, self.next))
        if self.next == None:
            return hash((self.data, None))
        else:
            return hash((self.data, self.next.data))

    def add_next(self, data):
        n = Node(data)
        self.next = n

class LinkedList:
    """def __init__(self):
        self.root = None"""

    def __init__(self, data_list = []):
        self.root = None
        for x in data_list:
            self.append(x)

    def __repr__(self):
        slist = [str(x)+' ' for x in self.to_list()]
        return ''.join(slist)

    def __eq__(self, other):
        return other and self.root == other.root

    def __ne__(self, other):
        return not self.__eq__(other)

    def append(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            n = self.root
            while n.next != None:
                n = n.next
            n.add_next(data)

    def append_node(self, node):
        if self.root == None:
            self.root = node
        else:
            n = self.root
            while n.next != None:
                n = n.next
            n.next = node

    def clear(self):
        self.root = None
        
    def to_list(self):
        li = []
        n = self.root
        while n != None:
            li.append(n.data)
            n = n.next
        return li

    def tail(self):
        if self.root == None:
            return None
        n = self.root
        while n.next != None:
            n = n.next
        return n

    def get_node(self, index):
        i = 0
        n = self.root
        while n != None:
            if i == index:
                return n
            n = n.next
            i += 1
        return None

    """def print(self):
        n = self.root
        while n != None:
            print(n.data, end=' ')
            n = n.next
        print()"""

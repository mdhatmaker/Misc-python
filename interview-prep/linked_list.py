import sys

# https://www.geeksforgeeks.org/reverse-a-linked-list/


# Node class (for linked list)
class Node: 
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

# Linked List class 
class LinkedList: 
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        self.tail = None

    # Function to append a new node to the end of the linked list
    def append(self, data):
        n = Node(data)
        if self.tail == None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def push(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def print(self):
        n = self.head
        while n != None:
            print(n.data, '-> ', end='')
            n = n.next
        print()

    # Function to reverse the linked list 
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        


# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    li1 = LinkedList() 
    
    li1.append(1)
    li1.append(2)
    li1.append(3)
    li1.print()

    li2 = LinkedList()
    li2.push(1)
    li2.push(2)
    li2.push(3)
    li2.print()

    li1.reverse()
    li1.print()

    li2.reverse()
    li2.print()

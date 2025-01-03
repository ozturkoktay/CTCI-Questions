class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_the_beginning(self, data):
        new_node = Node()
        
        if self.head == None:
            self.head = new_node
            return
        else: 
            new_node.next = self.head
            self.head = new_node
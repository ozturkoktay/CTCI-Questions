class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        if not self.head:
            return

        # If the head node itself holds the key
        if self.head.data == key:
            self.head = self.head.next
            return

        # Search for the key in the list
        current = self.head
        while current.next and current.next.data != key:
            current = current.next

        if current.next:
            current.next = current.next.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        def reverse_recursive(node, prev=None):
            if not node:
                return prev
            next_node = node.next
            node.next = prev
            return reverse_recursive(next_node, node)

        self.head = reverse_recursive(self.head)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
ll = SinglyLinkedList()

# Add elements
ll.add(10)
ll.add(20)
ll.add(30)

# Display the list
print("Original List:")
ll.display()  # Output: 10 -> 20 -> 30 -> None

# Search for an element
print("Search for 20:", ll.search(20))  # Output: True
print("Search for 40:", ll.search(40))  # Output: False

# Reverse the list
ll.reverse()
print("Reversed List:")
ll.display()  # Output: 30 -> 20 -> 10 -> None

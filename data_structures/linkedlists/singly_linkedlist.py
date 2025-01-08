class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        def add_recursive(node, data):
            if not node:
                return Node(data)
            node.next = add_recursive(node.next, data)
            return node
        self.head = add_recursive(self.head, data)

    def delete(self, key):
        def delete_recursive(node, key):
            if not node:
                return None
            if node.data == key:
                return node.next
            node.next = delete_recursive(node.next, key)
            return node
        self.head = delete_recursive(self.head, key)

    def search(self, key):
        def search_recursive(node, key):
            if not node:
                return False
            if node.data == key:
                return True
            return search_recursive(node.next, key)
        return search_recursive(self.head, key)

    def reverse(self):
        def reverse_recursive(node, prev=None):
            if not node:
                return prev
            next_node = node.next
            node.next = prev
            return reverse_recursive(next_node, node)
        self.head = reverse_recursive(self.head)

    def display(self):
        def display_recursive(node):
            if not node:
                print("None")
                return
            print(node.data, end=" -> ")
            display_recursive(node.next)
        display_recursive(self.head)


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

# Delete an element
ll.delete(20)
print("After Deleting 20:")
ll.display()  # Output: 30 -> 10 -> None

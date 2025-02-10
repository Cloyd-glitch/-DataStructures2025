class Node:
    def __init__(self, data):
        """Initializes a node with data and a pointer to the next node."""
        self.data = data  # Stores the value
        self.next = None  # Pointer to the next node (default is None)


class LinkedList:
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None  # Head of the linked list

    def insert(self, data):
        """Inserts a new node with the given data at the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Add the new node at the end

    def display(self):
        """Returns a list of all values in the linked list."""
        values = []
        current = self.head
        while current:
            values.append(current.data)  # Collect the data from each node
            current = current.next  # Move to the next node
        return values


# Example usage
ll1 = LinkedList()
ll1.insert(100)
ll1.insert(200)
print(ll1.display())  # Output: [100, 200]
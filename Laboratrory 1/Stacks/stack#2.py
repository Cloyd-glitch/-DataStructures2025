class StackContainer:
    def __init__(self):
        self.items_list = []

    def insert(self, element):            # insert() Adds an element to the top of the stack container.
        self.items_list.append(element)

    def extract(self):                    # extract() Removes and returns the top element from the stack container (if it's not empty).
        if not self.is_empty():
            return self.items_list.pop()  # Checks if the container is empty before extraction.
        return "Container is empty"
    
    def is_empty(self):                   # Checks if the container is empty.
        return len(self.items_list) == 0
    
    def view_top(self):                   # view_top() Returns the top element without removing it.
        return self.items_list[-1] if not self.is_empty() else "Container is empty"


container = StackContainer()
container.insert("X")
container.insert("Y")
print(container.view_top())   # Returns "Y" without removing it.

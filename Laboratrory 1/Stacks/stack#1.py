class Container:
    def __init__(self):                # Initializes an empty container.
        self.items = []

    def add(self, element):             # add() Inserts an element at the top of the container.
        self.items.append(element)

    def remove(self):                   # remove() Removes and returns the top element from the container (if it's not empty).
        if not self.is_empty():
            return self.items.pop()     # Checks if the container is empty before removal.
        return "Container is empty"
    
    def is_empty(self):                 # Verifies if the container has any elements.
        return len(self.items) == 0
    
# Example Usage:
container1 = Container()
container1.add(10)
container1.add(20)
print(container1.remove())  # Removes and returns 20

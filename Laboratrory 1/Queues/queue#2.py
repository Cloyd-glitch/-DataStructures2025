from collections import deque  # Using deque for efficient append and pop operations

class CustomQueue:
    def __init__(self):  # Constructor to initialize an empty queue
        self.items = deque()  # Renamed 'queue' to 'items' for clarity
    
    def add_item(self, item):  # Renamed 'enqueue' to 'add_item' for readability
        self.items.append(item)  # Adds an item to the end of the queue
    
    def remove_item(self):  # Renamed 'dequeue' to 'remove_item' for readability
        if not self.is_empty():
            return self.items.popleft()  # Removes and returns the first item
        return "The queue is currently empty"  # Updated message for clarity
    
    def is_empty(self):  # Checks if the queue is empty
        return len(self.items) == 0

# Example usage
my_queue = CustomQueue()
my_queue.add_item("Apple")
my_queue.add_item("Banana")
print(my_queue.remove_item())  # Prints "Apple" since it's the first element in the queue
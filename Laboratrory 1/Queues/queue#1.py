from collections import deque  # Double-ended queue for fast insertions and deletions from both ends


class Queue:
    def __init__(self):
        """Initializes an empty queue."""
        self.queue = deque()

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the first item from the queue.
        Returns 'Queue is empty' if the queue has no elements."""
        if not self.is_empty():
            return self.queue.popleft()  # Remove and return the leftmost item
        return "Queue is empty"

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0


# Example usage
queue1 = Queue()
queue1.enqueue(12)
queue1.enqueue(18)
print(queue1.dequeue())  # Output: 12 (since it's the first element in the queue)   
class Array:
    def __init__(self):
        """Initializes an empty array."""
        self.array = []

    def insert(self, value):
        """Adds a new value to the end of the array."""
        self.array.append(value)

    def delete(self, index):
        """Removes and returns the element at the given index.
        Returns 'Invalid index' if the index is out of bounds."""
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        return "Invalid index"


# Example usage
arr1 = Array()
arr1.insert(1)
arr1.insert(2)
print(arr1.delete(0))  # Output: 1 (deletes and returns the element at index 0)
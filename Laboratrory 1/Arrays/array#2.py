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
            return self.array.pop(index)  # Fixed typo: 'poop' -> 'pop'
        return "Invalid index"


# Example usage
arr2 = Array()
arr2.insert("Hello")
arr2.insert("World")
print(arr2.delete(1))  # Output: World (deletes and returns the element at index 1)
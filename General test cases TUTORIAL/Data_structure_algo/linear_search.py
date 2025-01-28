
# Linear Search (Array Traversal)
# Searches for an element in a list.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Target not found

# Example
arr = [10, 20, 30, 40, 50]
target = 30
print("Found at index:", linear_search(arr, target))


# Efficiently searches for an element in a sorted list using divide and conquer.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [10, 20, 30, 40, 50]
target = 40
print("Found at index:", binary_search(arr, target))

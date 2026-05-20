# 1. Find the largest element
def find_max(arr):
    return max(arr)

# 2. Reverse an array
def reverse_array(arr):
    return arr[::-1]

# 3. Check if array is sorted
def is_sorted(arr):
    return arr == sorted(arr)

# Testing
print(find_max([3, 1, 7, 2, 9]))        # Output: 9
print(reverse_array([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
print(is_sorted([1, 2, 3, 4, 5]))       # Output: True
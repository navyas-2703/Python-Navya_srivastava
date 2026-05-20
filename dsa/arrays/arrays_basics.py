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




# 4. Find second largest element
def second_largest(arr):
    arr = list(set(arr))  # remove duplicates
    arr.sort()
    return arr[-2]

# 5. Find duplicates in array
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    return duplicates

# 6. Rotate array by k steps
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# 7. Two Sum - find pair that adds to target
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# Testing
print(second_largest([3, 1, 7, 2, 9]))         # Output: 7
print(find_duplicates([1, 2, 3, 2, 4, 3]))     # Output: [2, 3]
print(rotate_array([1, 2, 3, 4, 5], 2))        # Output: [4, 5, 1, 2, 3]
print(two_sum([2, 7, 11, 15], 9))              # Output: [0, 1]
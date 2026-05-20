# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 3. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 4. Check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# 5. Find most frequent character
def most_frequent_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

# Testing
print(reverse_string("hello"))               # Output: olleh
print(is_palindrome("racecar"))              # Output: True
print(count_vowels("Hello World"))           # Output: 3
print(is_anagram("listen", "silent"))        # Output: True
print(most_frequent_char("programming"))     # Output: g
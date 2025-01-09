# Python List Summary: Key Points to Remember

# 1. Creating Lists
# Create a list
fruits = ["apple", "banana", "cherry"]

# Empty list
empty_list = []

# List with mixed data types
mixed = [1, "hello", 3.14]

# 2. Accessing and Modifying Elements
# Access by index
print(fruits[0])  # Output: apple

# Negative indexing
print(fruits[-1])  # Output: cherry

# Slicing
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Modify an element
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# 3. Adding and Removing Elements
# Append a single element
fruits.append("orange")

# Insert an element at a specific position
fruits.insert(1, "grape")

# Remove a specific element
fruits.remove("cherry")

# Remove the last element
fruits.pop()

# Clear all elements
fruits.clear()

# 4. Common Operations
# Length of a list
print(len(fruits))  # Output: 0 (after clearing)

# Concatenation
combined = [1, 2] + [3, 4]
print(combined)  # Output: [1, 2, 3, 4]

# Repetition
repeated = ["hello"] * 3
print(repeated)  # Output: ['hello', 'hello', 'hello']

# Membership testing
print("apple" in fruits)  # Output: False

# 5. Sorting and Reversing
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Sorts in place
print(numbers)  # Output: [1, 1, 3, 4, 5]

numbers.reverse()  # Reverses in place
print(numbers)  # Output: [5, 4, 3, 1, 1]

# 6. Key Properties
# - Lists are ordered.
# - Allow duplicate elements.
# - Mutable (can be modified).

# Final Tip: Use lists for dynamic, ordered collections of data!

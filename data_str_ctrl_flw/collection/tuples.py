# Python Tuple Summary: Key Points to Remember

# 1. Creating Tuples
# Create a tuple
person = ("John", 30, "New York")

# Single-element tuple (note the comma)
single_element = (42,)

# Empty tuple
empty_tuple = ()

# 2. Accessing Elements
# Access by index
print(person[0])  # Output: John

# Negative indexing
print(person[-1])  # Output: New York

# Slicing
print(person[1:3])  # Output: (30, 'New York')

# 3. Properties of Tuples
# - Tuples are immutable (cannot be modified after creation).
# - Allow duplicate elements.

# 4. Common Operations
# Concatenation
new_tuple = person + ("USA",)
print(new_tuple)  # Output: ('John', 30, 'New York', 'USA')

# Repetition
repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Membership testing
print("John" in person)  # Output: True

# Count occurrences of a value
print(person.count("John"))  # Output: 1

# Find index of a value
print(person.index(30))  # Output: 1

# 5. Use Cases
# - Fixed, ordered collections of data.
# - Data that should not change (e.g., coordinates, constants).

# Final Tip: Tuples are memory-efficient and faster than lists for immutable data!

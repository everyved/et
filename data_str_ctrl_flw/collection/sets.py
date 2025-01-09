# Python Set Summary: Key Points to Remember

# 1. Creating Sets
# Create a set
numbers = {1, 2, 3, 4, 5}  # Set with elements
empty_set = set()  # Create an empty set ({} creates a dictionary)

# Duplicate elements are automatically removed
duplicates = {1, 2, 2, 3}  # Result: {1, 2, 3}

# 2. Accessing Elements
# Membership testing (sets are unordered)
print(3 in numbers)  # True
print(10 in numbers)  # False

# 3. Adding and Removing Elements
# Add a single element
numbers.add(6)  # Adds 6 to the set

# Add multiple elements
numbers.update([7, 8])  # Adds 7 and 8

# Remove an element (raises error if not found)
numbers.remove(3)

# Discard an element (does not raise error if not found)
numbers.discard(10)

# Clear the set
numbers.clear()

# 4. Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union: Combine elements from both sets
print(set_a | set_b)  # {1, 2, 3, 4, 5}

# Intersection: Common elements in both sets
print(set_a & set_b)  # {3}

# Difference: Elements in A but not in B
print(set_a - set_b)  # {1, 2}

# Symmetric Difference: Elements in either set but not both
print(set_a ^ set_b)  # {1, 2, 4, 5}

# 5. Key Properties
# - Sets are unordered.
# - Sets do not allow duplicates.
# - Membership testing is efficient (O(1)).

# Final Tip: Use `frozenset` if you need an immutable set.

# Python Dictionary Summary: Key Points to Remember

# 1. Creating Dictionaries
# Create a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Empty dictionary
empty_dict = {}

# 2. Accessing and Modifying Elements
# Access a value using its key
print(person["name"])  # Output: John

# Use get() to avoid KeyError
print(person.get("country", "Unknown"))  # Output: Unknown

# Add or update a key-value pair
person["country"] = "USA"

# Remove a key-value pair
person.pop("age")  # Removes the key 'age'

# 3. Common Methods
# Keys, values, and items
print(person.keys())    # Get all keys
print(person.values())  # Get all values
print(person.items())   # Get all key-value pairs

# Check if a key exists
print("name" in person)  # True

# Clear all elements
person.clear()

# 4. Key Properties
# - Keys must be unique.
# - Keys must be immutable (e.g., strings, numbers, tuples).
# - Dictionaries are ordered (Python ≥ 3.7).

# Final Tip: Use dictionaries for fast lookups and mappings!

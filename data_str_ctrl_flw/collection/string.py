# Python String Summary: Key Points to Remember

# 1. Creating Strings
# Single and double quotes
string1 = 'Hello'
string2 = "World"

# Multiline string
multiline = '''This is
a multiline
string.'''

# 2. Accessing and Slicing Strings
# Access by index
print(string1[0])  # Output: H

# Negative indexing
print(string1[-1])  # Output: o

# Slicing
print(string2[1:4])  # Output: orl

# 3. Common String Methods
# Convert to uppercase
print(string1.upper())  # Output: HELLO

# Convert to lowercase
print(string1.lower())  # Output: hello

# Split into a list of words
words = "This is a test".split()
print(words)  # Output: ['This', 'is', 'a', 'test']

# Join a list of strings
joined = " ".join(words)
print(joined)  # Output: This is a test

# Replace a substring
print(string2.replace("World", "Python"))  # Output: Python

# Strip whitespace
print("   trimmed   ".strip())  # Output: trimmed

# 4. Formatting Strings
# f-strings (Python >= 3.6)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Using format()
print("My name is {} and I am {} years old.".format(name, age))

# 5. Key Properties
# - Strings are immutable (cannot be changed after creation).
# - Can be iterated over like a sequence.

# Final Tip: Use strings for text manipulation and representation!

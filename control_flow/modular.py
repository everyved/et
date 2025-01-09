# Python Tutorial: Modular Programming, Conditional Statements, and Loops

# 1. Modular Programming (Subroutines)
# - Functions are used to modularize code into reusable subroutines.
# - Use `def` to define a function.

# Example:
def greet(name):
    """This function greets the user."""
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))  # Output: Hello, Alice!

# Example with multiple parameters and a return value:
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(f"Sum: {result}")  # Output: Sum: 12

# Functions can also include default arguments:
def greet_with_default(name="Guest"):
    return f"Welcome, {name}!"

print(greet_with_default())  # Output: Welcome, Guest!
print(greet_with_default("Bob"))  # Output: Welcome, Bob!

# Essentials Tutorial: Basic Programming Elements of Python

# 1. Variables and Constants
# Variables: Used to store data that can change during program execution.
x = 10  # Variable storing an integer
y = "Hello"  # Variable storing a string

# Constants: Use naming conventions (uppercase) to define constants.
PI = 3.14159  # Approximate value of Pi
GRAVITY = 9.8  # Earth's gravity in m/s^2

# 2. Identifiers
# Identifiers are the names used for variables, constants, functions, etc.
# Example:
my_variable = 42  # Valid identifier

# Rules for Writing Identifiers:
# - Must begin with a letter (A-Z, a-z) or an underscore (_).
# - Can be followed by letters, digits (0-9), or underscores.
# - Cannot use Python keywords (e.g., `if`, `else`, `while`).
# - Case-sensitive (e.g., `myVar` and `myvar` are different).

# Invalid Identifiers (Examples):
# 1variable = 10  # Starts with a digit
# my-variable = 5  # Contains a special character ('-')

# 3. Typecasting or Type Conversion
# Converting one data type to another in Python.
# Implicit Conversion: Python automatically converts data types.
result = 5 + 4.5  # Integer and float -> Float (9.5)

# Explicit Conversion: Programmer manually converts data types.
x = "10"
y = int(x)  # Converts string "10" to integer 10
z = float(y)  # Converts integer 10 to float 10.0
print(z)  # Output: 10.0

# 4. Indentation
# Python uses indentation to define code blocks (no braces or keywords like `end`).
# Correct Indentation:
if True:
    print("This is indented")

# Incorrect Indentation:
# if True:
# print("This will cause an IndentationError")

# 5. Comments
# Comments are used to explain the code and are ignored during execution.
# Single-line comment:
# This is a single-line comment.

# Multi-line comment:
"""
This is a 
multi-line comment.
"""

# 6. Primitive Data Types
# Python's primitive data types include:
# - Integer: `int`
num = 10

# - Float: `float`
price = 19.99

# - String: `str`
name = "Python"

# - Boolean: `bool`
is_valid = True

# - NoneType: `None`
value = None

# Check data types using `type()`:
print(type(num))  # Output: <class 'int'>

# 7. Writing Command Line Programs in Python
# Command-line programs take input from the user and display output.
# Example: Adding two numbers

# Uncomment the below lines to run interactively
# num1 = float(input("Enter the first number: "))  # User input as float
# num2 = float(input("Enter the second number: "))  # User input as float
# print(f"The sum is: {num1 + num2}")  # Display the result

# Key Points to Remember:
# - Follow the rules for identifiers.
# - Use indentation correctly to avoid syntax errors.
# - Use comments for better code readability.
# - Understand primitive data types and how to perform typecasting.
# - Write command-line programs using `input()` and `print()` for user interaction.

# Final Tip: Master these basics to build a solid foundation for Python programming!

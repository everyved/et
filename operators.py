# Essentials Tutorial: Operators in Python and Taking User Input

# 1. Arithmetic Operators
# Used to perform basic mathematical operations.
# + : Addition
x = 5 + 3  # Result: 8
# - : Subtraction
y = 10 - 7  # Result: 3
# * : Multiplication
z = 4 * 2  # Result: 8
# / : Division
div = 10 / 3  # Result: 3.333...
# % : Modulus (remainder)
mod = 10 % 3  # Result: 1
# // : Floor division (quotient without remainder)
floor_div = 10 // 3  # Result: 3
# ** : Exponentiation (power)
power = 2 ** 3  # Result: 8

# 2. Relational Operators
# Used to compare two values (returns True or False).
# > : Greater than
print(5 > 3)  # True
# < : Less than
print(5 < 3)  # False
# >= : Greater than or equal to
print(5 >= 5)  # True
# <= : Less than or equal to
print(3 <= 5)  # True
# == : Equal to
print(5 == 5)  # True
# != : Not equal to
print(5 != 3)  # True

# 3. Logical Operators
# Used to combine conditional statements (returns True or False).
# and : True if both conditions are True
print(5 > 3 and 10 > 5)  # True
# or : True if at least one condition is True
print(5 > 3 or 10 < 5)  # True
# not : Inverts the boolean value
print(not(5 > 3))  # False

# 4. Membership Operators
# Used to check if a value is in a sequence (e.g., list, string).
# in : True if value is in the sequence
print("a" in "apple")  # True
# not in : True if value is not in the sequence
print("z" not in "apple")  # True

# 5. Taking User Input
# Use the `input()` function to get input from the user (as a string).
# Example: Adding two numbers
# Uncomment below lines to run interactively
# num1 = float(input("Enter the first number: "))  # Convert input to float
# num2 = float(input("Enter the second number: "))  # Convert input to float
# print(f"The sum is: {num1 + num2}")

# Key Points to Remember:
# - Arithmetic operators perform basic math.
# - Relational operators compare values and return boolean results.
# - Logical operators combine or invert conditions.
# - Membership operators check for the presence of elements in sequences.
# - Use `input()` to take user input, and convert it to the required data type using `int()`, `float()`, etc.

# Final Tip: Practice combining these operators with conditions and user inputs to build interactive programs!

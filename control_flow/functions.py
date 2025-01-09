# Python Tutorial: User-Defined Functions and Advanced Concepts

# 1. User-Defined Functions
# - Functions modularize code into reusable components.
# - Use `def` keyword to define a function.

# 1.1 No Value Pass and No Return
# - A function that neither takes arguments nor returns a value.
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# 1.2 Value Pass and No Return
# - A function that takes arguments but does not return a value.
def greet_name(name):
    print(f"Hello, {name}!")

# Call the function
greet_name("Alice")  # Output: Hello, Alice!

# 1.3 Value Pass and Return
# - A function that takes arguments and returns a value.
def add(a, b):
    return a + b

result = add(5, 7)
print(f"Sum: {result}")  # Output: Sum: 12

# 2. Function with Default Arguments
# - Default values are used if arguments are not provided.
def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")

# Call the function
greet_with_default()       # Output: Welcome, Guest!
greet_with_default("Bob")  # Output: Welcome, Bob!

# 3. Function with Variable Arguments
# - `*args` for positional arguments and `**kwargs` for keyword arguments.

# Example with *args
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10

# Example with **kwargs
def print_details(**kwargs):
    print('\nthese are items:',kwargs.items())
    print('\n')
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

# 4. Higher-Order Functions
# - Functions that take other functions as arguments or return functions.

# Example: Passing a function as an argument
def apply_function(func, value):
    return func(value)

def square(x):
    return x ** 2

print(apply_function(square, 5))  # Output: 25

# Example: Returning a function
def multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by

double = multiplier(2)
print(double(10))  # Output: 20

# 5. List Comprehension
# - A concise way to create lists using a single line of code.

# Example: Square of numbers
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Example: Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Example: Nested list comprehension
matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Final Tip: Combine these techniques to create reusable, efficient, and concise Python programs!

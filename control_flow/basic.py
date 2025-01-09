# Python Control Flow Tutorial: Sequential, Branching, and Iteration

# 1. Sequential Control Flow
# - Code is executed line by line in the order it is written.

# Example:
print("Step 1: Start")
print("Step 2: Process")
print("Step 3: End")

# Output:
# Step 1: Start
# Step 2: Process
# Step 3: End

# 2. Branching or Conditional Control Flow
# - Code execution depends on conditions (if, elif, else).

# Example:
number = 10
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# Output (if number = 10):
# Positive number

# Example with nested conditions:
age = 18
if age >= 18:
    if age >= 21:
        print("Adult")
    else:
        print("Young Adult")
else:
    print("Minor")

# Output (if age = 18):
# Young Adult

# 3. Iteration or Repetition
# - Repeat a block of code using loops (for, while).

# 3.1 For Loop
# - Used to iterate over a sequence (e.g., list, string, range).

# Example:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5

# Example with range():
for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# 3.2 While Loop
# - Repeats as long as a condition is True.

# Example:
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5

# 3.3 Loop Control Statements
# - `break`: Exit the loop immediately.
# - `continue`: Skip the current iteration and move to the next.

# Example with break:
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# Output:
# 1
# 2
# 3
# 4

# Example with continue:
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output:
# 1
# 2
# 4
# 5

# Final Tip: Understand the control flow structure to determine how the program behaves and use loops and conditions effectively for problem-solving.



# Identiy Operators in Python

# Identity operators are used to compare the memory locations of two objects.
# In Python, there are two identity operators: is and is not.

# 1. is Operator
# The is operator returns True if both variables point to the same object and False otherwise.

# example:
# check if two variables point to the same object
x = 5
y = 5
print(x is y)  # True

# Explanation: Both x and y point to the same object (5), so the result is True.

# example:
# check if two variables point to the same object
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # False

# Explanation: Although x and y have the same values, they point to different objects in memory, so the result is False.

# 2. is not Operator
# The is not operator returns True if both variables do not point to the same object and False otherwise.

# example:
# check if two variables do not point to the same object
x = 5
y = 5
print(x is not y)  # False

# Explanation: Both x and y point to the same object (5), so the result is False.

# example:
# check if two variables do not point to the same object
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)  # True

# Explanation: Although x and y have the same values, they point to different objects in memory, so the result is True.

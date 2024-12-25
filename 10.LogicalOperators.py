# Logical Operators in Python

# 1. and Operator
# The 'and' operator returns True if both statements are true
a = True
b = False
print("a and b:", a and b)  # Output: False

# Explanation: Since 'b' is False, the result of 'a and b' is False.

# 2. or Operator
# The 'or' operator returns True if at least one of the statements is true
a = True
b = False
print("a or b:", a or b)  # Output: True

# Explanation: Since 'a' is True, the result of 'a or b' is True.

# 3. not Operator
# The 'not' operator returns True if the statement is false
a = True
print("not a:", not a)  # Output: False

# Explanation: Since 'a' is True, 'not a' returns False.

# Combining Logical Operators
# You can combine logical operators to form complex expressions
a = True
b = False
c = True
print("a and b or c:", a and b or c)  # Output: True

# Explanation: 'a and b' is False, but 'False or c' is True since 'c' is True.

# Using Logical Operators with Comparisons
x = 10
y = 20
z = 30
print("x < y and y < z:", x < y and y < z)  # Output: True

# Explanation: Both 'x < y' and 'y < z' are True, so the result is True.
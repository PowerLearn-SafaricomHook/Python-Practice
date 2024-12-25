# Assignment Operators in Python
# Assignment operators are used to assign values to variables. 
# In Python, there are several types of assignment operators, 
# each performing a different operation on the variable's value.


# Basic assignment
x = 10
print("x =", x)  # Output: x = 10

# Add and assign
# This operator adds the right operand to the left operand and assigns the result to the left operand.
x += 5
print("x += 5 ->", x)  # Output: x += 5 -> 15

# Subtract and assign
# This operator subtracts the right operand from the left operand and assigns the result to the left operand.
x -= 3
print("x -= 3 ->", x)  # Output: x -= 3 -> 12

# Multiply and assign
x *= 2
print("x *= 2 ->", x)  # Output: x *= 2 -> 24

# Divide and assign
# This operator divides the left operand by the right operand and assigns the result to the left operand.
x /= 4
print("x /= 4 ->", x)  # Output: x /= 4 -> 6.0

# Modulus and assign
# This operator divides the left operand by the right operand and assigns the remainder to the left operand.
x %= 5
print("x %= 5 ->", x)  # Output: x %= 5 -> 1.0

# Floor division and assign
# This operator divides the left operand by the right operand and assigns the quotient to the left operand.
x //= 2
print("x //= 2 ->", x)  # Output: x //= 2 -> 0.0

# Exponent and assign
# This operator raises the left operand to the power of the right operand and assigns the result to the left operand.
x **= 3
print("x **= 3 ->", x)  # Output: x **= 3 -> 0.0

# Bitwise AND and assign
# This operator performs a bitwise AND operation on the left and right operands and assigns the result to the left operand.
x = 10
x &= 7
print("x &= 7 ->", x)  # Output: x &= 7 -> 2

# Bitwise OR and assign
x |= 5
print("x |= 5 ->", x)  # Output: x |= 5 -> 7

# Bitwise XOR and assign
x ^= 3
print("x ^= 3 ->", x)  # Output: x ^= 3 -> 4

# Bitwise right shift and assign
x >>= 1
print("x >>= 1 ->", x)  # Output: x >>= 1 -> 2

# Bitwise left shift and assign
x <<= 2
print("x <<= 2 ->", x)  # Output: x <<= 2 -> 8



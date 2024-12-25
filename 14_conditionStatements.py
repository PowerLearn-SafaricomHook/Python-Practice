
# If Statement in python
# If statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block),
#  else we process another block of statements (called the else-block).

# Syntax:
# if condition: 
#     # block of statements
# else:
#     # block of statements

# Example:

a = 33
b= 200

if b>a:
    print("b is greater than a")

# Elif

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

# else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Syntax:

# if condition:
#     # block of statements
# elif condition:
#     # block of statements
# else:
#     # block of statements

# Example:

a=33
b= 21

if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")


# Short Hand If

# If you have only one statement to execute, you can put it on the same line as the if statement.

# Syntax:
# if condition: statement

# Example:

if a>b: print("a is greater than b")

# Short Hand If ... Else

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# Syntax:
# statement if condition else statement

# Example:

print("A") if a>b else print("B")




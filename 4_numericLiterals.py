
# Numeric Literals in python
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

# Integer literals
a = 0b1010 # Binary Literals
b = 100 # Decimal Literal
c = 0o310 # Octal Literal
d = 0x12c # Hexadecimal Literal

# Float literals
float_1 = 10.5
float_2 = 1.5e2

# Complex literals
# Complex literals are written as a + bj.
# Where a is the real part and b is the imaginary part.

x = 3.14j

# print(a, b, c, d)
# print(float_1, float_2)
# print(x, x.imag, x.real)


#String literals in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

msg = "Python is fun"
char = "C"

# multiline string 
# You can assign a multiline string to a variable by using three quotes:
multiline = """This is a multiline string with more than one line code."""

# unicode string
# You can use unicode characters in a string

unicode= u"\u00dcnic\u00f6de"

# raw string
# Raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\) as a literal character. This is useful when we want to have a string that contains backslash and don’t want it to be treated as an escape character.

raw = r"raw \n string!"

print(msg)
print(char)
print(multiline)
print(unicode)
print(raw)





# importing modules in python

# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

# There are actually three different ways to define a module in Python:
# A module can be written in Python itself.
# A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
# A built-in module is intrinsically contained in the interpreter, like the itertools module.

# To use a module, we use the import keyword followed by the module name.
# For example, to import the module math, which contains many standard mathematical functions, we can do:

import math
print(math.sqrt(16))  # 4.0
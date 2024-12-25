

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

# When the interpreter encounters an import statement, it imports the module if the module is present in the search path.
# A search path is a list of directories that the interpreter searches before importing a module.
# When you install Python, a directory is created containing standard modules and packages. This directory is added to the search path.
# You can see the list of directories in the search path by importing the sys module and printing the sys.path variable.

import sys
print(sys.path)

# You can add your own directories to the search path by setting the PYTHONPATH environment variable.
# The PYTHONPATH variable has a value that is a string with a list of directories separated by the system path separator (os.pathsep).
# On Windows, the default path separator is a semicolon (;), and on Unix, it is a colon (:).

# For example, to add the directory /home/me/mypython to the search path, you can add the following line to your .bashrc file:

# export PYTHONPATH="/home/me/mypython"

# This will add the directory /home/me/mypython to the search path.


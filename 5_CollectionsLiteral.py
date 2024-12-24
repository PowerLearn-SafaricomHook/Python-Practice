

# Collections literals
# Python has four types of collections literals:
# List literals
# Tuple literals
# Dict literals
# Set literals

# List literals

# List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0.

# List literals are written within square brackets [ ]. It is a mutable collection of items. You can add, remove, or delete elements from the list.
# example:

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]


# nested list
# nested list is a list within a list 
my_list = ["mouse", [8, 4, 6], ['a']]
# print(my_list)

# Tuple literals
# Tuple literals are written within parentheses ( ). 
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples).
# example:

# empty tuple
my_tuple = ()

# tuple of integers
my_tuple = (1, 2, 3)

# tuple with mixed data types
my_tuple = (1, "Hello", 3.4)

# nested tuple
# nested tuple is a tuple within a tuple
my_tuple = ("mouse", (8, 4, 6), ['a'])
# print(my_tuple)

# Dict literals
# Dict literals are written within curly braces { }. They can be used to store key-value pairs. 
# A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
# example:

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# print(my_dict)

# Set literals
# Set literals are written within curly braces { }. A set is an unordered collection of items. Every element is unique (no duplicates).
# example:

# set of integers
my_set = {1, 2, 3}

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

# When to use collections literals
# Use list literals when you need a mutable collection of items that may change in size.
# Use tuple literals when your collection of items should not change.
# Use dict literals when you need a collection of items that are stored as key-value pairs.
# Use set literals when you need an unordered collection of unique items.

# difference between list and tuple
# The main difference between lists and a tuples is the fact that lists are mutable whereas tuples are immutable.
#  A mutable data type means that a python object of this type can be modified. An immutable object can't.
#  This means that a list can be changed, but a tuple cannot.

# Diffrence between a set and a dictionary
# A set is an unordered collection of items. Every element is unique (no duplicates). 
# A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in set() function.

# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.




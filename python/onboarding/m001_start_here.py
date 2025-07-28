# This is a comment
"""
This can be considered a comment, but it's actually a multiline string literal.
Since it isn't assigned to a variable or used otherwise, it will be ignored.
"""

# Variables
x = 1
y, z = 2, 3 # y = 2, z = 3

a: int = 1 # this uses a type hint. I like type hints :)
print(a) # Python's print() automatically performs a to_string() operation

y = "hello world" # y used to be an int, but now it's a str
a: str = "hello world" # this works even with type hints, since the interpreter doesn't enforce them

# These are the data types in Python

# Boolean
my_bool: bool = True

# Numeric types
my_int: int = 0
print(1 + my_int)

my_float: float = 0.0
print(my_float - 5.6)

im_complicated: complex = 2+5j
print(im_complicated.__class__)
print(im_complicated.real + 3) # prints 5
print(im_complicated.imag + 3) # prints 8
print(im_complicated + (3+4j)) # prints 5+9j

# Text
my_str: str = "hello world"
print(my_str.__class__)
print(my_str[0])
print(my_str + ", and its seven seas")

# Sequence types
my_list: list = ["hi", "world", 2, 4.4]
my_list_2: list[str] = ["hi", "typed", "world", 2, 4.4] # str is just a suggestion, like the Pirate's Code, but probably should follow it anyway
print(my_list.__class__)
print(my_list[0])

my_tuple: tuple = (4, 5, 6, "hi tuple")
my_tuple_2: tuple[float] = (3.14, 6.78, 1.2345)
my_range: range = range(0, 100)
print(my_range.__class__)

# Prints every third element, starting at 0 (the first element)
for i in my_range:
    if i % 3 == 0:
        print(i)

# Dictionary
my_dict: dict = {
    1:"hi",
    "one":4,
    "key":"value", # trailing commas on multiline code are nice for version control
}

my_dict_2: dict[str, str] = {
    "name":"Jack",
    "occupation":"Captain",
    1:"key is not a str like suggested",
}

# Set types
my_set: set = {
    "thing",
    "other thing",
    2,
    3.4,
}

my_frozen_set: frozenset = {"frozen", "so cold", "can't move..."}
# The import statement in Python allows you to bring in and use code (like functions, classes, and variables) from other Python files or libraries. This way, you don’t need to rewrite code; you can simply "import" it.
import math
# Using math.sqrt to calculate the square root of 16
result = math.sqrt(16)
print(result)  # Output: 4.0

# This imports only a specific function, class, or variable from a module, allowing you to use it directly by name without needing a prefix.
from math import sqrt
result = sqrt(16)
print(result)  # Output: 4.0

# Sometimes, you might want to use a shorter name for a module. You can use 'as' to rename the module when importing.
# Using numpy's array function
import numpy as np

my_array = np.array([1, 2, 3])
print(my_array)  # Output: [1 2 3]

# Practice using both forms of import
import math  # Imports the entire math module
from random import randint  # Only imports randint from random

# Using math.pi
print("Pi:", math.pi)  # Output: 3.141592653589793

# Using randint directly
print("Random integer:", randint(1, 10))  # Output: A random number between 1 and 10

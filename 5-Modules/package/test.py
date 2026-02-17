# test.py inside package
from .maths import *
from package.maths import *
from .subpackages.mult import *
from package.subpackages.mult import *

print(addition(2, 3))
print(subtraction(5, 2))
print(multiplication(3, 4))

print("All imports worked correctly!")
 


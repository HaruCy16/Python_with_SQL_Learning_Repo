# PART 1: Using built-in modules

#sqrt
#value of pi
#random nums 1 - 10
import math
import random

#user input sqrt
user_input_sqrt = float(input("Enter a number to find its square root: "))
print("Square root of", user_input_sqrt, "is:", math.sqrt(user_input_sqrt))

#value of pi
print("Value of pi is:", math.pi)

#random number between 1 and 10
print("Random number between 1 and 10 is:", random.randint(1, 10))

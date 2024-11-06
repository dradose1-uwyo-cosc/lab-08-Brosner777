# Braxton Rosner
# UWYO COSC 1010
# 11/6.2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to: Read w3schools article on try functions. 
# 
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def get_float_input(prompt):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return "exit"
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return "exit"
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")
print(get_float_input(""))

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    if x_lower > x_upper:
        return False
    return [m * x + b for x in range(x_lower, x_upper + 1)]

while True:
    m = get_float_input("Enter the slope (m) or 'exit' to quit: ")
    if m == "exit":
        break
    b = get_float_input("Enter the y-intercept (b): ")
    x_lower = get_int_input("Enter the lower x bound: ")
    x_upper = get_int_input("Enter the upper x bound: ")
    if "exit" in [b, x_lower, x_upper]:  
        break

    result = slope_intercept(m, b, x_lower, x_upper)
    if result is False:
        print("Invalid bounds. Ensure lower bound is <= upper bound.")
    else:
        print("y values:", result)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def safe_sqrt(value):
    return value**0.5 if value >= 0 else None

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = safe_sqrt(discriminant)
    
    if sqrt_discriminant is None:
        return None, None
    
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2


while True:
    a = get_float_input("Enter the value for a (or type 'exit' to quit): ")
    if a == "exit":
        break

    b = get_float_input("Enter the value for b (or type 'exit' to quit): ")
    if b == "exit":
        break

    c = get_float_input("Enter the value for c (or type 'exit' to quit): ")
    if c == "exit":
        break
    
    root1, root2 = quadratic_formula(a, b, c)
    
    if root1 is None and root2 is None:
        print("The equation has no real roots.")
    else:
        print(f"The roots of the equation are: {root1} and {root2}")


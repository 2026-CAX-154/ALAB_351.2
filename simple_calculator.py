# ALAB 351.2 
# Part 2: User Interaction and Input
# Author: Eren Kim

# Create a Python script called simple_calculator.py to perform basic calculations using user input.
# Note: Exception handling has not yet been covered in class.

# Ask user to enter two integers, floats, or both. 
num1 = int(input("Enter an integer:"))
num2 = float(input("Enter a floating number:"))
print() # Print a blank line for better readability in the console.
# End of user input

# Perform basic arithmetic calculations using num1 and num2 values.
# Find the sum of num1 and num2. 
sum = num1 + num2
# Find the difference between num1 and num2.
difference = num1 - num2
# Find the product of num1 and num2.
product = num1 * num2
# Find the quotient of num1 and num2.
quotient = num1 / num2
# End of calculations

# Display calculation results in the console.
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")
print() # Print a blank line for better readability in the console.
# End of displaying results

# End of Python script

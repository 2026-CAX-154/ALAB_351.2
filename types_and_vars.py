# ALAB 351.2
# Author: Eren Kim

###############################################
# Part 1: Python Basics and Output Formatting

# The following code declares three variables (name, age, height) and prints out an introduction. 
name = "Alice" # name as a string
age = 25 # age in years (integer)
height = 1.5 # height in meters (float)
print() # Print a blank line for better readability. 

# Print out an introduction using string concatenation.
print("Hello, my name is " + name + ". I am " + str(age) + " years old and " + str(height) + " meters tall.")
# Print out the same introduction using an f-string.
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")
# End of introduction 

# Age calculations
# Calculate and print out the age in 5 years using an f-string.
print(f"\nIn 5 years, I will be {age + 5} years old. (f-string)")
# Calculate and print out age 1o years ago using string concatenation.
print(f"\nTen years ago, I was {age - 10} years old.")
# Calculate and print out age in 20 years using string concatenation and a separator.
print("\nIn twenty years, I will be", (age + 20), "years old.", sep=" ") 
# End of age calculations

# Calculate the area of a rectangle with width = 5.5 and height = 2.
width = 5.5 # width of the rectangle
height = 2  # height of the rectangle
print(f"\nThe area of a rectangle with width = {width} and height = {height} is {width * height} square units.") # Print out the rectangle area.
# End of rectangle calculation 



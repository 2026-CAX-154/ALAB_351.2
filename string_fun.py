# ALAB 351.2 
# Part 2: User Interaction and Input
# Author: Eren Kim

# This script accepts a word as user input to print out: 
# - the word length
# - the word in all uppercase
# - the word repeated 3 times (on the same line)
# - the word repeated 3 times (on separate lines)

word = str(input("Enter a word to play with: ")) # Prompt user for a word
print("The word length is", len(word), ".") # Print word length
print("The word in all uppercase is", word.upper()) # Print word in uppercase
print("The word printed out 3 times in a row is",word * 3) # Print word 3 times in a row
print("The word printed out 3 times on separate lines is:") # Print word 3 times on separate lines
print(word, word, word, sep="\n")

# End of Python script 

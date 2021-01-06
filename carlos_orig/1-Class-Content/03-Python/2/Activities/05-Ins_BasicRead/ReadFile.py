# Store the file path associated with the file
import os
filepath = os.path.join('Resources', 'input.txt')

# Open the file in "read" mode ('r') and
# store the contents in the variable "text"
with open(filepath, 'r') as text:

    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


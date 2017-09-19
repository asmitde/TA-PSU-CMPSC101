# Question 3 - Variable name sanitization
# Asmit De
# 04/28/2017

# Input string
var = input('Enter a variable name: ')

# Assume var to be valid initially
valid = True

# Loop through the characters in the variable name
for ch in var:

    # If the character is not an alphabet, digit or underscore
    if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9' or ch == '_'):
        
        # variable name is invalid
        valid = False

        # break out of the loop - no need to check the other characters
        break

# Check if the first character is a digit
if '0' <= var[0] <= '9':
    # Then variable name is invalid
    valid = False

# Display result based on the status of the valid flag
if valid:
    print(var, 'is valid')
else:
    print(var, 'is not valid')

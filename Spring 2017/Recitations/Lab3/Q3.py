
# Recitation Lab 3 Question 3: Program to convert from uppercase to lowercase
# Author: Asmit De
# Date: 02/02/2017

# Input uppercase letter
ucletter = input('Enter an uppercase letter: ')

# Convert entered letter to ASCII
ucl_ascii = ord(ucletter)

# Determine the ascii difference between lowercase and uppercase letters.
shift = ord('a') - ord('A')

# Calculate the ascii value of the corresponding lowercase letter
lcl_ascii = ucl_ascii + shift

# Convert ascii to letter
lcletter = chr(lcl_ascii)

# Display lowercase letter
print('In lowercase it is:', lcletter)

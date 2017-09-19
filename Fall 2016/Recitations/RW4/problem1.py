# Name: Asmit De
# Section: 001/002
# PSU ID: aud311
# Lab Assignment: Recitation Week 4 - Problem 1
# Date: 09/15/2016
# Description: Display the character associated with an ASCII code

# Prompt the user to enter an ASCII code and save it in a variable
ascii_code = int(input('Enter an ASCII value: '))

# Obtain the corresponding character
ascii_char = chr(ascii_code)

# Display the corresponding character
print('The character for ASCII code', ascii_code, 'is', ascii_char)

# Name: Asmit De
# ID: aud311
# Date: 09/20/2016
# Assignment: Homework 2, Problem 9
# Description: Program to convert a 6-bit binary number to decimal

# Prompt the user to enter a 6-bit binary number
binary = int(input('Enter a 6-bit binary number: '))

# Extract the bits and form the decimal number
decimal = 0
decimal += (binary % 10) * (2 ** 0)
binary //= 10
decimal += (binary % 10) * (2 ** 1)
binary //= 10
decimal += (binary % 10) * (2 ** 2)
binary //= 10
decimal += (binary % 10) * (2 ** 3)
binary //= 10
decimal += (binary % 10) * (2 ** 4)
binary //= 10
decimal += (binary % 10) * (2 ** 5)

# Display the decimal number
print('The decimal equivalent is', decimal)

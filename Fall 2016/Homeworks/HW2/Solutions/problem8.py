# Name: Asmit De
# ID: aud311
# Date: 09/20/2016
# Assignment: Homework 2, Problem 8
# Description: Program to reverse a number

# Prompt the user to enter an eight digit number
num = int(input('Enter an eight digit number: '))

# Extract the digits and form the reverse number
reverse = 0
reverse += (num % 10) * (10 ** 7)
num //= 10
reverse += (num % 10) * (10 ** 6)
num //= 10
reverse += (num % 10) * (10 ** 5)
num //= 10
reverse += (num % 10) * (10 ** 4)
num //= 10
reverse += (num % 10) * (10 ** 3)
num //= 10
reverse += (num % 10) * (10 ** 2)
num //= 10
reverse += (num % 10) * (10 ** 1)
num //= 10
reverse += (num % 10) * (10 ** 0)

# Display the reversed number
print('The reverse is', reverse)

# Name: Asmit De
# ID: aud311
# Date: 09/20/2016
# Assignment: Homework 2, Problem 7
# Description: Program to calculate sum of digits

# Prompt the user to enter an integer between 0 ans 100
num = int(input('Enter an integer between 0 and 100: '))

# Extract the digits
d0 = num % 10
d1 = num // 10

# Display the sum of the digits
print('Sum of the digits is', d0 + d1)

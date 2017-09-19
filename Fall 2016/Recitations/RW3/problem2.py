# Name: Asmit De
# Section: 001/002
# PSU ID: aud311
# Lab Assignment: Recitation Week 3 - Problem 2
# Date: 09/08/2016
# Description: Calculate sum, product and average of any three numbers

# Prompt the user to enter three numbers and save them in variables
print('Please enter three numbers:')
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Calculate the sum, product and average
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3

# Print the result
print('The sum is:', sum)
print('The product is:', product)
print('The average is:', average)

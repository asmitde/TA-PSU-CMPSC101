# Name: Asmit De
# Section: 001/002
# PSU ID: aud311
# Lab Assignment: Recitation Week 3 - Problem 4
# Date: 09/08/2016
# Description: Swap values between variables

# Prompt the user to enter two numbers and save them in variables
print('Please enter two numbers:')
num1 = input('num1 = ')
num2 = input('num2 = ')

# Perform the swap using a temporary variable
temp = num1    # <- This ensures that the value of num1 is not lost
num1 = num2
num2 = temp    # <- Restore the value of num1 into num2

# Display the contents of the variables after swap
print('\nAfter swapping:\nnum1 =', num1, '\nnum2 =', num2)

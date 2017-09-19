# Recitation Lab 5 Question 1: Program to find smallest power of 2 greater than or equal to a number
# Author: Asmit De
# Date: 03/02/2017

# Input number
num = int(input('Enter a number: '))

# Initialize variable to the lowest power of 2
powervalue = 2

# Run loop until powervalue becomes greater than or equal to num
while powervalue < num:
    
    # Generate the next power of 2 and update powervalue (just double it!)
    powervalue *= 2

# Display final powervalue
print('The smallest power of 2 greater than or equal to', num, 'is', powervalue)
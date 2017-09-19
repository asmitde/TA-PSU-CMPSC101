
# Recitation Lab 4 Question 2: Program to calculate sum of squares of first n natural numbers
# Author: Asmit De
# Date: 02/23/2017

# Input n
n = int(input('Enter the value of n: '))

# Initialize sum
sum = 0

# Initialize loop counter
i = 1

# Run loop n times
while i <= n:

    # Calculate square of i
    iSquared = i ** 2

    # Update sum by adding iSquared
    sum += iSquared

    # Increment loop counter
    i += 1

# Display result
print('Sum of squares of first', n, 'natural numbers is', sum)

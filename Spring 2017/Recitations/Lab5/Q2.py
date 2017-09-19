# Recitation Lab 5 Question 2: Program to check if a number is in base-3
# Author: Asmit De
# Date: 03/02/2017

# Input number
num = int(input('Enter a number: '))

# Set a boolean variable assuming the number entered is in base-3
isBase3 = True

# Copy the number to another variable - we will modify this later, so the original is saved
n = num

# Run a loop to extract digits from the number and check if the digits are valid base-3 digits
while n > 0:
    
    # Extract the last digit from n
    digit = n % 10

    # Check if the digit is not a valid base-3 digit (0, 1, or 2).
    if digit >= 3:
        # Then our assuption was incorrect. So reset isBase3 to False.
        isBase3 = False

        # Also, there is no point checking the remaining digits, so break out of the loop.
        break

    # If the digit is a valid one, reduce the number by discarding the last digit.
    # Go to the beginning of the loop to keep checking the remaining digits.
    # The number will eventually become 0, which will terminate the loop.
    n //= 10

# Now check the status of isBase3. If all the digits in n were 0, 1, or 2,
# isBase3 will remain set at True. Print accordingly.
if isBase3 == True:
    print(num, 'is a valid base-3 number')
else:
    print(num, 'is not a valid base-3 number')
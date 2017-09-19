# Recitation Lab 5 Question 3: Program to accept only a power of 5 number
# Author: Asmit De
# Date: 03/02/2017


# Initialize boolean variable isPowerOf5 to False.
# This is to enter the loop for the fisrt time.
isPowerOf5 = False

# Run the loop as long a isPowerOf5 is False.
# This means the user has not yet entered a power of 5 number.
while isPowerOf5 == False:

    # Input number
    num = int(input('Please enter a power of 5: '))

    # Initialize variable to the lowest power of 5
    powervalue = 5

    # Run loop until powervalue becomes greater than or equal to num
    while powervalue < num:
        # Generate the next power of 5 and update powervalue
        powervalue *= 5

    # Now check the last value in powervalue. If it is equal to num,
    # it means that num is a valid power of 5.
    if powervalue == num:
        
        # Print success
        print('You entered a power of 5!')
       
        # Set the sentinel variable to True so that the loop terminates
        isPowerOf5 = True

    else:
        # The user did not enter a power of 5. Display error and repeat loop.
        print('You did not enter a power of 5.')
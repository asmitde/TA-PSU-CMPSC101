# Question 2 - Implement function to find the first factor of a number
# Asmit De
# 04/28/2017


## Function definition for factor ----##
# Parameters:   n (int)
# Return:       i or -1 (int) - The first number b/w 2 and n-1 which divides n, or -1 if no factors exist.
#
def factor(n):

    # Run loop from 2 to n-1
    for i in range(2, n):
        
        # If i perfectly divides n, i.e., i is a factor of n
        if n % i == 0:

            # We found the smallest factor of n.
            # Return the factor, i. Note that the
            # function terminates here.
            return i

    # If the code reaches this point, then we haven't found any factor
    return -1

##---- Function definition ends ##


## Main program code ##

# Enter number from the user
num = int(input('Enter n: '))

# Call the factor function with num as argument
# and store the returned value in divisor.
divisor = factor(num)

# Display the smallest factor
print('The smallest divisor is:', divisor)

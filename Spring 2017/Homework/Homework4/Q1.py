# Question 1 - Implement function to calculate formula: f = x^3 + x + y
# Asmit De
# 04/28/2017


# Function definition for cubic ----##
# Parameters:   x (int)
#               y (int)
# Return:       result (int) - result of x^3 + x + y
#
def cubic(x, y):
    
    # Compute formula
    result = x ** 3 + x + y

    # Return result
    return result

##---- Function definition ends ##


## Main program code ##

# Enter two numbers from the user
n1 = int(input('Enter x: '))
n2 = int(input('Enter y: '))

# Call the cubic function with n1 and n2 as arguments
# and store the returned value in res.
res = cubic(n1, n2)

# Display the computed result
print('The result is:', res)

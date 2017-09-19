# Question 6 - Multiplication table
# Asmit De
# 03/24/2017

# Enter number
n = int(input('Enter a number: '))

# Initialize multiplier
multiplier = 1

# Run loop 10 times
while multiplier <= 10:
    
    # Calculate product
    product = n * multiplier

    # Print
    print(n, 'x', multiplier, '=', product)

    # Increment multiplier
    multiplier += 1
    
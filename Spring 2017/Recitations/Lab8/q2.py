
# Recitation Lab 8 Question 2 - Modified Fibonacci numbers in a given range
# Author: Asmit De
# Date: 04/06/2017

# Enter lower bound
lb = int(input('Enter lower bound: '))

# Enter b
ub = int(input('Enter upper bound: '))

# Initialize modified fibonacci list to contain the first 2 numbers of the sequence
fibonacci = [1, 1]

# Initialize the 3-rd fibonacci number
i_fibo = 1

# Generate fibonacci numbers till the upper bound
while i_fibo <= ub:
    
    # If the previously generated number is greater than 
    # or equal to the lower bound, print the number
    if i_fibo >= lb:
        print(i_fibo, end = ' ')
    
    # Also, put the number in the fibonacci list
    fibonacci.append(i_fibo)
    
    # Generate the next number in sequence.
    # The i-th fibonacci number is the sum of the i-1, i-2 and i-3 fibonacci numbers
    i_fibo = fibonacci[-1] + fibonacci[-2] + fibonacci[-3]

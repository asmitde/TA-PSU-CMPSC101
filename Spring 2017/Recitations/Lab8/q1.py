
# Recitation Lab 8 Question 1 - N-th number in modified Fibonacci
# Author: Asmit De
# Date: 04/06/2017

# Enter n
n = int(input('Enter value of n: '))

# Initialize modified fibonacci list to contain the first 3 numbers of the sequence
fibonacci = [1, 1, 1]

# Run loop for generating the 4-th to N-th numbers in the sequence
for i in range(3, n):
    
    # The i-th fibonacci number is the sum of the i-1, i-2 and i-3 fibonacci numbers
    i_fibo = fibonacci[i - 1] + fibonacci[i - 2] + fibonacci[i - 3]
    
    # Put the i-th fibonacci number in the list
    fibonacci.append(i_fibo)

# Display the n-th fibonacci number - this will of course be the last element of the list
print('\nThe', n, '-th number in the sequence is', fibonacci[-1])

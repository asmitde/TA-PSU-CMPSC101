
# Recitation Lab 4 Question 1: Program to print the first n letters of the alphabet
# Author: Asmit De
# Date: 02/23/2017

# Input n
n = int(input('Enter the value of n (1 - 26): '))

# Determine the ascii value of the 0-th (yes, get used to counting from 0) letter of the alphabet
base = ord('A')

# Initlialize loop counter. We will also use the counter as an offset to
# determine the ascii value of the letters to be printed.
i = 0

# Run loop n times
while i < n:

    # Determine the ascii value of the i-th letter
    ascii = base + i

    # Convert ascii to letter
    letter = chr(ascii)

    # Print letter, ensuring the next print happens on the same line
    print(letter, end='')

    # Increment loop counter
    i += 1

# Dummy print to generate a newlinw at the end
print()

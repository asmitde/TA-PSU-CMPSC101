
# Recitation Lab 4 Question 3: Program to print alternate lower/upper case letter triangle
# Author: Asmit De
# Date: 02/23/2017

# Input n
n = int(input('Enter the value of n (1 - 26): '))

# Initialize loop counter. We will also use this counter as line numbers for printing,
# as well as to calculate the ascii of letters to be printed.
i = 0

# Determine the ascii values of the 0-th uppercase and lowercase letters of the alphabet
baseUC = ord('A')
baseLC = ord('a')

# Run loop n times
while i < n:

    # Set the base ascii acc. to the line number. Even numbered lines are in lowercase
    # and odd numbered lines are in uppercase. Remember, line number starts at 0.
    if i % 2 == 0:
        base = baseLC
    else:
        base = baseUC

    # Determine the ascii value of the i-th letter
    ascii = base + i

    # Convert ascii to letter
    letter = chr(ascii)

    # We need to repeat the letter i + 1 times for line number i. Note the relation
    # between the line number and the number of repetitions.
    letterRepeated = letter * (i + 1)

    # Print letter string
    print(letterRepeated)

    # Increment loop counter
    i += 1

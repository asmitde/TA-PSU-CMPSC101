
# Recitation Lab 7 Question 2 - Find most frequently occuring element in a list
# Author: Asmit De
# Date: 03/23/2017

# Enter number of elements in list
n = int(input('Enter number of elements in list: '))

# Initialize empty list
numbers = []

# Run loop n times to enter n elements in the list
for i in range(n):
    e = int(input('Enter element #' + str(i) + ': '))
    numbers.append(e)

# Display the list
print('\nThe list you entered is:\n', numbers)

# Initialize variables for tracking most frequent element and count
mostFreqElem = None
mfeCount = 0

# Iterate through list elements
for e in numbers:

    # Obtain count of element e
    count = numbers.count(e)

    # Update mostFreqElem and count if a higher count is found
    if count > mfeCount:
        mfeCount = count
        mostFreqElem = e

# Print the most frequent element
print('\nThe most common element is', e)

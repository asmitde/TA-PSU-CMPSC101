
# Recitation Lab 7 Question 1 - Square elements in a list
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

# Iterate over the list elements, accessing by index
for i in range(n):

    # Get the element at index i
    e = numbers[i]

    # Square the element value
    eSquared = e ** 2

    # Store the squared value back in the same position
    numbers[i] = eSquared

# Display the modified list
print('\nThe list with numbers squared is:\n', numbers)

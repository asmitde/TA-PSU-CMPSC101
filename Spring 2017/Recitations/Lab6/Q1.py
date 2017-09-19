
# Recitation Lab 6 Question 1 - Interleave elements from lists
# Author: Asmit De
# Date 03/16/2017

# Input number of elements in list
n = int(input('Enter number of list elements: '))

# Initialize empty lists
list1 = []
list2 = []
list3 = []

# Populate list1 with multiples of 5
i = 1
while i <= n:
    
    # Generate i-th multiple of 5
    multiple = 5 * i

    # Add multiple to list1
    list1.append(multiple)

    # Increment i
    i += 1


# Populate list2 with odd numbers
oddn = 1
i = 1
while i <= n:
    
    # Add i-th odd number to list2
    list2.append(oddn)

    # Generate next odd number
    oddn += 2

    # Increment i
    i += 1


# Populate list3 with elements from list1 and list2.
# Note that list index starts at 0.
i = 0
while i < n:
    
    # Access i-th elements from list1 and list2
    elem1 = list1[i]
    elem2 = list2[i]

    # Add the two elements to list3
    list3.append(elem1)
    list3.append(elem2)

    # Increment i
    i += 1


# Print the lists
print('List1:', list1)
print('List2:', list2)
print('List3:', list3)

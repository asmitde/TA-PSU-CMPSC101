# Question 1 - List intersection
# Asmit De
# 04/28/2017

# Input list data and form lists
user_input = input('Enter a numbers for the 1st list: ')
list1 = [int(e) for e in user_input.split()]
user_input = input('Enter a numbers for the 2nd list: ')
list2 = [int(e) for e in user_input.split()]

# Create empty intersection list
intersection = []

# Loop through 1st list picking each element
for e in list1:

    # If the element is there in the 2nd list, add it to the intersection list
    if e in list2:  # Note that this is equivalent to running a loop to search for an element
        intersection.append(e)

# Display the intersection list
print('The numbers common to both lists are:', end = ' ')
for e in intersection:
    print(e, end = ' ')
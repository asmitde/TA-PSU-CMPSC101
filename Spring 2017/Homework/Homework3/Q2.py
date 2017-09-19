# Question 2 - List union
# Asmit De
# 04/28/2017

# Input list data and form lists
user_input = input('Enter a numbers for the 1st list: ')
list1 = [int(e) for e in user_input.split()]
user_input = input('Enter a numbers for the 2nd list: ')
list2 = [int(e) for e in user_input.split()]

# Create empty union list
union = []

# Loop through combined list of list1 and list2 picking each element
for e in list1 + list2:
    # If the element is not already present in the union list, add it to the union list
    if e not in union:  # Note that this is equivalent to running a loop to search for an element
        union.append(e)

# Display the intersection list
print('The distinct numbers in both lists are:', end = ' ')
for e in union:
    print(e, end = ' ')
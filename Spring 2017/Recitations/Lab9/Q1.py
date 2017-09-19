
# Recitation Lab 9 Question 1 - Merge lists in sorted order
# Author: Asmit De
# Date: 04/13/2017

# Enter list data
user_string = input('Enter elements in 1st list in sorted order: ')
list1 = [int(n) for n in user_string.split()]
user_string = input('Enter elements in 2nd list in sorted order: ')
list2 = [int(n) for n in user_string.split()]

# Determine the length of the two lists
n1 = len(list1)
n2 = len(list2)

# Initialize empty list for merged data
list3 = []

# Initialize pointers for the two lists
i = 0
j = 0

# Loop until either one of the lists run out
while i < n1 and j < n2:
    
    # Pick the elements based on the current pointer position
    e1 = list1[i]
    e2 = list2[j]

    # Pick the smallest element out of the two and add that to the new list.
    # Increment the corresponding pointer.
    if e1 <= e2:
        list3.append(e1)
        i += 1
    else:
        list3.append(e2)
        j += 1

# If there are any elements left in the first list,
# pick them and put them in the new list. Since the
# list is already sorted, there is no need for any
# comparison, and the remaining elements are bound to be
# larger than the existing elements in the new list.
list3.extend(list1[i:n1])

# Do the same for the second list also
list3.extend(list2[j:n2])

# Display the merged list
print("Merged list: ", list3)

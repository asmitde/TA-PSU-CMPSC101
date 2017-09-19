# Question 4 - Find repeated number
# Asmit De
# 04/28/2017

######################################## Solution 1 #########################################

# Input n
n = int(input('Enter n: '))

# Enter list data
user_input = input('Enter the list: ')
nums = [int(n) for n in user_input.split()]

# Initialize a list of n elements to all False.
# present[i] = True/False denotes if the number i+1
# from the nums list is recorded to be present at least once.
present = [False] * n

# Loop through the numbers in the nums list
for e in nums:

    # Using the number e itself as an index (e-1, because index starts at 0) 
    # of the list present, check if e has already been marked as present (true).
    if present[e - 1]:
        # This means that we have come across e earlier.
        # Hence this is the repeat number.
        print('The repeated number is:', e)

        # Break out of the Loop
        break

    # Else if the presence of e is marked as false,
    else:
        # update it to true - we found the 1st occurrence.
        present[e - 1] = True

#############################################################################################

######################################## Solution 2 #########################################

# Input n
n = int(input('Enter n: '))

# Enter list data
user_input = input('Enter the list: ')
nums = [int(n) for n in user_input.split()]

# Calculate the sum of all the numbers from 1 to n
sum_n = n * (n + 1) // 2

# Calculate the sum of the numbers entered
sum_all = 0
for e in nums:
    sum_all += e

# The difference between the two will be the repeated number
rep = sum_all - sum_n

# Display the repeated number
print('The repeated number is:', rep)

#############################################################################################

# Recitation Lab 6 Question 2 - Find second highest score from a list
# Author: Asmit De
# Date 03/16/2017

# Input number of students
n = int(input('Enter number of students: '))

# Create a list by entering the scores
scores = []
i = 0
while i < n:
    s = int(input('Enter score of student #' + str(i) + ': '))
    scores.append(s)
    i += 1

# Initialize variables to keep track of highest and second highest score
highest = 0
secondHighest = 0

# Traverse through the score list and update the highest and second highest scores
i = 0
while i < n:
    
    # Get the i-th element from the list - the current score
    s = scores[i]

    # Case 1: If the current score is greater than the highest score found so far,
    if s > highest:
        
        # the highest score now becomes the second highest
        secondHighest = highest

        # and the new highest score is the current score.
        highest = s

    # Case 2: If the current score is less than highest but greater than
    # the second highest score found so far,
    elif s > secondHighest:
        
        # the current score becomes the new second highest score.
        secondHighest = s

    # Increment i
    i += 1


# Print the second highest score
print('\nThe second highest score is', secondHighest)

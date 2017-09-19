
# Recitation Lab 10 Question 1 - Find average of best 4 scores
# Author: Asmit De
# Date: 04/20/2017


# Function definition for drop1
# Parameters:   scores (string) - space separated score list
# Return:       avg_score (float) - average of the best 4 scores
#
# The function finds the lowest score among 5 scores and returns the average
# of the remaining 4 scores. If there are fewer than 5 scores, it
# assumes the missing scores to be 0. If there are more than 5 scores
# it only works on the first 5 scores and ignores the rest.
def drop1(scores):

    # Generate the list of scores from the string
    scorelist = [float(s) for s in scores.split()]

    # If the scorelist has less than 5 numbers, fill remaining with 0
    l = len(scorelist)
    if l < 5:
        scorelist += [0] * (5 - l)
    
    # Else rebuild scorelist with just the 1st 5 numbers
    else:
        scorelist = scorelist[:5]

    # Initialize variables for minimum score and sum
    min_score = scorelist[0]
    sum_scores = 0

    # Pick each element from the list and add them.
    # Also update the min_score everytime.
    for s in scorelist:
        sum_scores += s
        if s < min_score:
            min_score = s

    # Subtract the minimum score from the sum
    sum_scores -= min_score

    # Calculate the average of 4 scores
    avg_score = sum_scores / 4

    # Return the calculated average
    return avg_score


# Main function
def main():

    # Enter list data
    inpscores = input('Enter scores: ')

    # Call the drop1 function with the input as parameter
    # and print out the return value
    print('The average after dropping is', drop1(inpscores))


# Call main() to run the program
main()
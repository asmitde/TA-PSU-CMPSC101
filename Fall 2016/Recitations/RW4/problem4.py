# Name: Asmit De
# Section: 001/002
# PSU ID: aud311
# Lab Assignment: Recitation Week 4 - Problem 4
# Date: 09/15/2016
# Description: Calculate percentages of males/females in class

# Prompt the user to enter the number of males and females
males = int(input('Enter the number of males: '))
females = int(input('Enter the number of females: '))

# Calculate the fraction of males and females in class
total = males + females
male_pc = males / total
female_pc = females / total

# Display the percentage of males and females in class
print('Percentage of males =', format(male_pc, '.2%'))
print('Percentage of females =', format(female_pc, '.2%'))

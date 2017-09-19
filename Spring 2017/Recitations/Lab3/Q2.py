
# Recitation Lab 3 Question 2: Program to convert days to years, weeks and days
# Author: Asmit De
# Date: 02/02/2017

totaldays = int(input('Enter total number of days: '))

years = totaldays // 365
remainingdays = totaldays % 365

weeks = remainingdays // 7
days = remainingdays % 7

print(totaldays, 'days is', years, 'years', weeks, 'weeks and', days, 'days')

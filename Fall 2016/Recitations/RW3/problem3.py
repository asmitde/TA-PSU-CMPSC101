# Name: Asmit De
# Section: 001/002
# PSU ID: aud311
# Lab Assignment: Recitation Week 3 - Problem 3
# Date: 09/08/2016
# Description: Convert total seconds to hours, minutes and seconds

# Prompt the user to enter seconds
total_seconds = int(input('Please enter seconds: '))

# Calculate the hours minutes and seconds
hours = total_seconds // 3600
rem_seconds = total_seconds % 3600
minutes = rem_seconds // 60
seconds = rem_seconds % 60

# Print the result
print('You entered:', hours, 'hour(s),', minutes, 'minute(s) and', \
      seconds, 'second(s)')

#########################################################################
# Name: Asmit De                                                        #
# ID: aud311                                                            #
# Date: 09/07/2016                                                      #
# Assignment: Homework 1, Problem 8                                     #
# Description: Program to compute surface area and volume of a cylinder #
#########################################################################


# Input the radius
radius = float(input('Enter the radius of the cylinder: '))

# Input the length
length = float(input('Enter the length of the cylinder: '))

# Set the value of PI to 3.14
PI = 3.14

# Calculate the area
area = PI * radius * radius

# Calculate the volume
volume = area * length

# Display the result
print('Area =', area, '\nVolume =', volume)

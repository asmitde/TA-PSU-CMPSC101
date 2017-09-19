# HW1 Q8 - Calculate travel time between two cities
# Author(s): Asmit De
# Date: 01/27/2017

# Input source and destination from user
src = input("Enter source city: ")
dest = input("Enter destination city: ")

# Input distance b/w source and destination
print("Enter distance between", src, "and", dest, "(miles): ", end = "")
distance = float(input())

# Input car speed
speed = float(input("Enter average speed of car (mph): "))

# Calculate expected travel time
time = distance / speed

# Output expected travel time
print("\nExpected time required to travel from", src, "to", dest, "is", time, "hours")

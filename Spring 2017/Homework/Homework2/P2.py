# Question 2 - Determine age group
# Asmit De
# 03/24/2017

# Input age
age = int(input('Enter your age: '))

# Age less than or equal to 1 : Infant
if age <= 1:
    ageGroup = 'infant'
# Age is between 1 and 13 : Child
elif age < 13:
    ageGroup = 'child'
# Age is greater than or equal to 13 but less than 20 : Teenager
elif age < 20:
    ageGroup = 'teenager'
# Age is more than 20 :  Adult
else:
    ageGroup = 'adult'

# Display age group
print('You are a', ageGroup)
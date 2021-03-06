# Get the weight and height from the user
weight = float(input('Enter weight (lb): '))
height = float(input('Enter height (in): '))

# Calculate the body mass index
BMI = weight / (height ** 2) * 703

# Display BMI
print('BMI:', format(BMI, '.2f'))

# Determine and display weight category
if BMI > 25:
    print('You are overweight.')
elif BMI >= 18.5:
    print('You are normal.')
else:
    print('You are underweight.')

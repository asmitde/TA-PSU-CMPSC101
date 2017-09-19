# Question 8 - Calculate power
# Asmit De
# 03/24/2017

# Enter number and exponent
num = int(input('Enter a number 1: '))
exp = int(input('Enter a number 2: '))

# Initialize loop counter and result
i = 1
result = 1

# Run loop exp times
while i <= exp:

    # Calculate num raised to i
    result *= num

    # Increment i
    i += 1

# Display result
print(num, '**', exp, 'is', result)

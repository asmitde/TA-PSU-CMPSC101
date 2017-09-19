# Question 7 - Calculate factorial
# Asmit De
# 03/24/2017

# Enter number
n = int(input('Enter a number: '))

# Initialize factorial and loop counter
fact = 1
i = 2

# Run loop till n
while i <= n:

    # Calculate i factorial
    fact *= i

    # Increment i
    i += 1

# Print factorial
print(n, 'factorial is', fact)

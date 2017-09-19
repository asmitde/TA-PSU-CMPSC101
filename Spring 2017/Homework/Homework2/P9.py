# Question 9 - Convert binary to decimal
# Asmit De
# 03/24/2017

# Enter binary
binary = int(input('Enter binary number: '))

# Duplicate variable for modification
b = binary

# Initialize decimal
decimal = 0

# Initialize bit position
i = 0

# Set a valid flag
isValid = True

# Extract each bit and form the decimal number
while b > 0:

    # Extract last bit
    bit = b % 10

    # Check if bit is valid (0 or 1)
    if bit > 1:
        
        # Reset valid flag
        isValid = False

        # Exit loop - no point in continuing
        break

    # Form partial decimal
    decimal += (2 ** i) * bit

    # Reduce binary number discarding last bit
    b //= 10

    # Increment bit position
    i += 1

# Check status of valid and print decimal
if isValid == True:
    print('The decimal equivalent of', binary, 'is', decimal)
else:
    print(binary, 'is not a valid binary number')
    
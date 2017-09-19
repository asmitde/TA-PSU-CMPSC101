# Question 3 - Calculator with menu
# Asmit De
# 03/24/2017

# Display menu
print('You can choose between:')
print('1) Add two numbers')
print('2) Multiply three numbers')
print('3) Multiply a number and a string')

# Enter option
op = input('Choose an option: ')

# If user chose 1
if op == '1':
    
    # Input the numbers
    n1 = int(input('Enter number 1: '))
    n2 = int(input('Enter number 2: '))

    # Calculate the sum
    sum = n1 + n2

    # Display result
    print('The answer is', sum)
    
# else if the user chose 2
elif op == '2':
    
    # Input the numbers
    print('Enter the three numbers:')
    n1 = int(input('Enter number 1: '))
    n2 = int(input('Enter number 2: '))
    n3 = int(input('Enter number 3: '))

    # Calculate the product
    product = n1 * n2 * n3

    # Display result
    print('The answer is', product)

# else if the user chose 3
elif op == '3':
    
    # Input the string and multiplier
    text = input('Enter string: ')
    mult = int(input('Enter number: '))

    # Replicate string
    result = text * mult

    # Display result
    print('The answer is', result)

# else if the user typed anything else
else:

    # Display error
    print('Invalid option')
